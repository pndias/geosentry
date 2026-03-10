import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, CircleMarker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Shield, Globe, TrendingUp, AlertTriangle, Menu, X, Filter, ChevronRight, Activity } from 'lucide-react';
import './index.css';

// --- Tipos ---
type Categoria = 'Militar' | 'Politica' | 'Economica' | 'Religiosa/Simbólica';

interface Evento {
  id: number;
  titulo: string;
  categoria: Categoria;
  resumo_analitico: string;
  coordenadas?: { lat: number; lon: number };
  impacto: number;
  fontes_citadas: string[];
}

// --- Componentes ---

const Sidebar = ({ events, onEventClick, selectedCategory, setSelectedCategory, isOpen, toggleSidebar }: any) => (
  <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
    <div className="sidebar-header">
      <div className="logo">
        <Globe size={28} className="text-blue-500" />
        <span>GeoSentry</span>
      </div>
      <button className="close-btn mobile-only" onClick={toggleSidebar}><X /></button>
    </div>

    <div className="stats-grid">
      <div className="stat-card">
        <Shield size={16} />
        <span>Militares</span>
        <strong>{events.filter((e: any) => e.categoria === 'Militar').length}</strong>
      </div>
      <div className="stat-card">
        <TrendingUp size={16} />
        <span>Econômicos</span>
        <strong>{events.filter((e: any) => e.categoria === 'Economica').length}</strong>
      </div>
    </div>

    <div className="filter-section">
      <label><Filter size={14} /> Filtro Global</label>
      <select 
        value={selectedCategory} 
        onChange={(e) => setSelectedCategory(e.target.value)}
        className="modern-select"
      >
        <option value="all">Todas as Categorias</option>
        <option value="Militar">Militar</option>
        <option value="Politica">Política</option>
        <option value="Economica">Econômica</option>
        <option value="Religiosa/Simbólica">Religiosa/Simbólica</option>
      </select>
    </div>

    <div className="event-feed">
      {events.map((evento: Evento) => (
        <div key={evento.id} className="feed-item" onClick={() => onEventClick(evento)}>
          <div className="item-meta">
            <span className={`badge ${evento.categoria.toLowerCase().replace('/', '-')}`}>{evento.categoria}</span>
            <span className="impact">Impacto: {evento.impacto}</span>
          </div>
          <h3>{evento.titulo}</h3>
          <p>{evento.resumo_analitico.substring(0, 80)}...</p>
        </div>
      ))}
    </div>
  </aside>
);

const App = () => {
  const [events, setEvents] = useState<Evento[]>([]);
  const [filteredEvents, setFilteredEvents] = useState<Evento[]>([]);
  const [category, setCategory] = useState('all');
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [mapCenter, setMapCenter] = useState<[number, number]>([20, 0]);
  const [mapZoom, setMapZoom] = useState(2);

  useEffect(() => {
    fetch('/api/eventos')
      .then(res => res.json())
      .then(data => {
        setEvents(data);
        setFilteredEvents(data);
      })
      .catch(err => {
        console.error("Erro na busca:", err);
        // Fallback para localhost se o proxy falhar (ambiente de dev local)
        fetch('http://localhost:8000/eventos')
          .then(res => res.json())
          .then(data => {
            setEvents(data);
            setFilteredEvents(data);
          });
      });
  }, []);

  useEffect(() => {
    if (category === 'all') {
      setFilteredEvents(events);
    } else {
      setFilteredEvents(events.filter(e => e.categoria === category));
    }
  }, [category, events]);

  const handleEventClick = (evento: Evento) => {
    if (evento.coordenadas) {
      setMapCenter([evento.coordenadas.lat, evento.coordenadas.lon]);
      setMapZoom(5);
    }
  };

  return (
    <div className="dashboard-container">
      <button className="menu-toggle mobile-only" onClick={() => setSidebarOpen(true)}>
        <Menu />
      </button>

      <Sidebar 
        events={filteredEvents} 
        onEventClick={handleEventClick}
        selectedCategory={category}
        setSelectedCategory={setCategory}
        isOpen={sidebarOpen}
        toggleSidebar={() => setSidebarOpen(false)}
      />

      <main className="main-content">
        <header className="main-header">
          <div className="header-info">
            <Activity size={20} className="pulse" />
            <span>Sistemas de Monitoramento em Tempo Real</span>
          </div>
          <div className="user-profile">
            <span>Sentinela do Sul Global</span>
            <div className="avatar">GS</div>
          </div>
        </header>

        <div className="map-view">
          <MapContainer center={mapCenter} zoom={mapZoom} className="map-root" zoomControl={false}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {filteredEvents.map(evento => evento.coordenadas && (
              <CircleMarker 
                key={evento.id}
                center={[evento.coordenadas.lat, evento.coordenadas.lon]}
                radius={8 + evento.impacto * 2}
                fillColor={evento.categoria === 'Militar' ? '#ef4444' : '#3b82f6'}
                color="#fff"
                weight={1}
                fillOpacity={0.7}
              >
                <Popup>
                  <div className="modern-popup">
                    <h3>{evento.titulo}</h3>
                    <p>{evento.resumo_analitico}</p>
                    <div className="popup-footer">
                      <strong>Impacto {evento.impacto}/5</strong>
                      <span>Fontes: {evento.fontes_citadas.join(', ')}</span>
                    </div>
                  </div>
                </Popup>
              </CircleMarker>
            ))}
          </MapContainer>
        </div>
      </main>
    </div>
  );
};

export default App;
