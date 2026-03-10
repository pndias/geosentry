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
  switch(categoria) {
    case 'Militar': return '#ef4444'; // Red
    case 'Politica': return '#3b82f6'; // Blue
    case 'Economica': return '#22c55e'; // Green
    case 'Religiosa/Simbólica': return '#a855f7'; // Purple
    default: return '#3b82f6';
  }
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
              <div className="popup-footer">
                <strong>Impacto {evento.impacto}/5</strong>
                <span>{evento.fontes_citadas.join(', ')}</span>
              </div>
            </div>
          </Popup>
        </CircleMarker>
      ))}
    </MapContainer>
  );
};

export default React.memo(EventMap);
