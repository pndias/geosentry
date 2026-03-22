import React, { useEffect, useRef, useMemo } from 'react';
import { MapContainer, TileLayer, Circle, Popup, useMap, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Event } from '../types';

interface EventMapProps {
  events: Event[];
  mapCenter: [number, number];
  mapZoom: number;
  onViewChange?: (lat: number, lon: number, radiusKm: number) => void;
}

const MapController: React.FC<{ center: [number, number]; zoom: number }> = ({ center, zoom }) => {
  const map = useMap();
  useEffect(() => {
    map.flyTo(center, zoom, { duration: 1.5 });
  }, [center, zoom, map]);
  return null;
};

const ViewChangeEmitter: React.FC<{ onViewChange: (lat: number, lon: number, radiusKm: number) => void }> = ({ onViewChange }) => {
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const emitBounds = (map: L.Map) => {
    if (timerRef.current) clearTimeout(timerRef.current);
    timerRef.current = setTimeout(() => {
      const center = map.getCenter();
      const bounds = map.getBounds();
      const radiusKm = center.distanceTo(bounds.getNorthEast()) / 1000;
      onViewChange(center.lat, center.lng, radiusKm);
    }, 400);
  };

  useMapEvents({
    moveend: (e) => emitBounds(e.target),
    zoomend: (e) => emitBounds(e.target),
  });

  return null;
};

const getCategoryColor = (category: string) => {
  const normalized = category.toLowerCase();
  if (normalized.includes('military')) return '#dc2626';
  if (normalized.includes('political')) return '#2563eb';
  if (normalized.includes('economic')) return '#16a34a';
  if (normalized.includes('religious') || normalized.includes('symbolic')) return '#9333ea';
  return '#2563eb';
};

// Impact → consequence radius in meters
const getImpactRadius = (impact: number) => {
  const radii: Record<number, number> = { 1: 30000, 2: 60000, 3: 120000, 4: 250000, 5: 500000 };
  return radii[impact] || 60000;
};

const EventMap: React.FC<EventMapProps> = ({ events, mapCenter, mapZoom, onViewChange }) => {
  // Deduplicate by title, keeping highest impact instance
  const uniqueEvents = useMemo(() => {
    const map = new Map<string, Event>();
    for (const e of events) {
      const existing = map.get(e.title);
      if (!existing || e.impact > existing.impact) map.set(e.title, e);
    }
    return Array.from(map.values());
  }, [events]);

  return (
    <MapContainer center={mapCenter} zoom={mapZoom} className="map-root" zoomControl={false}>
      <TileLayer 
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" 
        attribution='&copy; OpenStreetMap'
      />
      <MapController center={mapCenter} zoom={mapZoom} />
      {onViewChange && <ViewChangeEmitter onViewChange={onViewChange} />}
      
      {uniqueEvents.map(event => event.coordinates && (
        <Circle 
          key={event.id}
          center={[event.coordinates.lat, event.coordinates.lon]}
          radius={getImpactRadius(event.impact)}
          fillColor={getCategoryColor(event.category)}
          color={getCategoryColor(event.category)}
          weight={2}
          fillOpacity={0.25}
          opacity={0.8}
        >
          <Popup>
            <div className="modern-popup">
              <h3 style={{ color: getCategoryColor(event.category) }}>{event.title}</h3>
              {event.context === 'Global Threats' && <span style={{ background: '#fff7ed', color: '#f97316', padding: '2px 6px', borderRadius: '4px', fontSize: '0.65rem', fontWeight: 700, textTransform: 'uppercase' }}>Global Threat</span>}
              <p>{event.analytical_summary}</p>
              <div className="popup-footer" style={{ flexDirection: 'column', gap: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <strong>Impact {event.impact}/5</strong>
                  <span>{event.cited_sources.join(', ')}</span>
                </div>
                {event.source_link && (
                  <div style={{ marginTop: '4px' }}>
                    <a 
                      href={event.source_link} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      style={{ color: '#3b82f6', textDecoration: 'none', fontSize: '0.8rem', display: 'flex', alignItems: 'center', gap: '4px' }}
                    >
                      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                      View Original Source
                    </a>
                  </div>
                )}
              </div>
            </div>
          </Popup>
        </Circle>
      ))}
    </MapContainer>
  );
};

export default React.memo(EventMap);
