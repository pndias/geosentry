import React, { useMemo } from 'react';
import { Shield, Globe, TrendingUp, X, Filter } from 'lucide-react';
import { Evento } from '../types';

interface SidebarProps {
  events: Evento[];
  onEventClick: (evento: Evento) => void;
  selectedCategory: string;
  setSelectedCategory: (category: string) => void;
  isOpen: boolean;
  toggleSidebar: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ 
  events, 
  onEventClick, 
  selectedCategory, 
  setSelectedCategory, 
  isOpen, 
  toggleSidebar 
}) => {

  const militarCount = useMemo(() => events.filter(e => e.categoria === 'Militar').length, [events]);
  const economicaCount = useMemo(() => events.filter(e => e.categoria === 'Economica').length, [events]);

  return (
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
          <strong>{militarCount}</strong>
        </div>
        <div className="stat-card">
          <TrendingUp size={16} />
          <span>Econômicos</span>
          <strong>{economicaCount}</strong>
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
        {events.map((evento) => (
          <div key={evento.id} className="feed-item" onClick={() => onEventClick(evento)}>
            <div className="item-meta">
              <span className={`badge ${evento.categoria.toLowerCase().replace('/', '-')}`}>{evento.categoria}</span>
              <span className="impact">Impacto: {evento.impacto}</span>
            </div>
            <h3>{evento.titulo}</h3>
            <p>{evento.resumo_analitico.substring(0, 80)}...</p>
          </div>
        ))}
        {events.length === 0 && <div className="text-center p-4 text-gray-500">Nenhum evento encontrado.</div>}
      </div>
    </aside>
  );
};

export default React.memo(Sidebar);
