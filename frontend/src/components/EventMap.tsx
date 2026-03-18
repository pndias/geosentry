import React, { useEffect } from 'react';
import { MapContainer, TileLayer, CircleMarker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Event } from '../types';

interface EventMapProps {
  events: Event[];
  mapCenter: [number, number];
  mapZoom: number;
}

const MapController: React.FC<{ center: [number, number]; zoom: number }> = ({ center, zoom }) => {
  const map = useMap();
  useEffect(() => {
    map.flyTo(center, zoom, { duration: 1.5 });
  }, [center, zoom, map]);
  return null;
};

const getCategoryColor = (category: string) => {
  const normalized = category.toLowerCase();
  if (normalized.includes('military')) return '#ef4444';
  if (normalized.includes('political')) return '#3b82f6';
  if (normalized.includes('economic')) return '#22c55e';
  if (normalized.includes('religious') || normalized.includes('symbolic')) return '#a855f7';
  return '#3b82f6';
};

const EventMap: React.FC<EventMapProps> = ({ events, mapCenter, mapZoom }) => {
  return (
    <MapContainer center={mapCenter} zoom={mapZoom} className="map-root" zoomControl={false}>
      <TileLayer 
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" 
        attribution='&copy; OpenStreetMap'
      />
      <MapController center={mapCenter} zoom={mapZoom} />
      
      {events.map(event => event.coordinates && (
        <CircleMarker 
          key={event.id}
          center={[event.coordinates.lat, event.coordinates.lon]}
          radius={8 + event.impact * 2.5}
          fillColor={getCategoryColor(event.category)}
          color="#ffffff"
          weight={1.5}
          fillOpacity={0.7}
        >
          <Popup>
            <div className="modern-popup">
              <h3 style={{ color: getCategoryColor(event.category) }}>{event.title}</h3>
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
        </CircleMarker>
      ))}
    </MapContainer>
  );
};

export default React.memo(EventMap);
