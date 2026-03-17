import React, { useEffect } from 'react';
import { MapContainer, TileLayer, CircleMarker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Evento } from '../types';

interface EventMapProps {
  events: Evento[];
  mapCenter: [number, number];
  mapZoom: number;
}

// Componente utilitário para mover o mapa quando o centro muda
const MapController: React.FC<{ center: [number, number]; zoom: number }> = ({ center, zoom }) => {
  const map = useMap();
  useEffect(() => {
    map.flyTo(center, zoom, { duration: 1.5 });
  }, [center, zoom, map]);
  return null;
};

const getCategoryColor = (categoria: string) => {
  const normalized = categoria.toLowerCase();
  if (normalized.includes('militar')) return '#ef4444';
  if (normalized.includes('politica')) return '#3b82f6';
  if (normalized.includes('economica')) return '#22c55e';
  if (normalized.includes('religiosa') || normalized.includes('simbólica')) return '#a855f7';
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
      
      {events.map(evento => evento.coordenadas && (
        <CircleMarker 
          key={evento.id}
          center={[evento.coordenadas.lat, evento.coordenadas.lon]}
          radius={8 + evento.impacto * 2.5}
          fillColor={getCategoryColor(evento.categoria)}
          color="#ffffff"
          weight={1.5}
          fillOpacity={0.7}
        >
          <Popup>
            <div className="modern-popup">
              <h3 style={{ color: getCategoryColor(evento.categoria) }}>{evento.titulo}</h3>
              <p>{evento.resumo_analitico}</p>
              <div className="popup-footer" style={{ flexDirection: 'column', gap: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <strong>Impacto {evento.impacto}/5</strong>
                  <span>{evento.fontes_citadas.join(', ')}</span>
                </div>
                {evento.link_fonte && (
                  <div style={{ marginTop: '4px' }}>
                    <a 
                      href={evento.link_fonte} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      style={{ color: '#3b82f6', textDecoration: 'none', fontSize: '0.8rem', display: 'flex', alignItems: 'center', gap: '4px' }}
                    >
                      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                      Ver Fonte Original
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
