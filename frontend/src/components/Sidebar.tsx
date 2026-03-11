// © 2026 Pablo Dias. Todos os direitos reservados.
import React, { useMemo, useState } from 'react';
import { Shield, Globe, TrendingUp, X, Filter, AlertTriangle, BookOpen, List } from 'lucide-react';
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

  const [activeTab, setActiveTab] = useState<'feed' | 'alertas' | 'fontes'>('feed');

  const militarCount = useMemo(() => events.filter(e => e.categoria === 'Militar').length, [events]);
  const highImpactEvents = useMemo(() => events.filter(e => e.impacto >= 4), [events]);
  
  // Agrupamento e contagem de fontes citadas
  const sourcesCount = useMemo(() => {
    const counts: Record<string, number> = {};
    events.forEach(e => {
      e.fontes_citadas.forEach(f => {
        counts[f] = (counts[f] || 0) + 1;
      });
    });
    return Object.entries(counts).sort((a, b) => b[1] - a[1]);
  }, [events]);

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
        <div className="stat-card" style={highImpactEvents.length > 0 ? { borderColor: '#ef4444', borderWidth: '1px', borderStyle: 'solid' } : {}}>
          <AlertTriangle size={16} color={highImpactEvents.length > 0 ? '#ef4444' : 'currentColor'} />
          <span>Alertas Críticos</span>
          <strong style={highImpactEvents.length > 0 ? { color: '#ef4444' } : {}}>{highImpactEvents.length}</strong>
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

      <div className="sidebar-tabs">
        <button className={`tab-btn ${activeTab === 'feed' ? 'active' : ''}`} onClick={() => setActiveTab('feed')}><List size={14}/> Feed</button>
        <button className={`tab-btn ${activeTab === 'alertas' ? 'active' : ''}`} onClick={() => setActiveTab('alertas')}><AlertTriangle size={14}/> Alertas</button>
        <button className={`tab-btn ${activeTab === 'fontes' ? 'active' : ''}`} onClick={() => setActiveTab('fontes')}><BookOpen size={14}/> Fontes</button>
      </div>

      <div className="event-feed">
        {activeTab === 'feed' && (
          <>
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
          </>
        )}

        {activeTab === 'alertas' && (
          <>
            {highImpactEvents.map((evento) => (
              <div key={evento.id} className="feed-item" onClick={() => onEventClick(evento)} style={{ borderColor: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.05)' }}>
                <div className="item-meta">
                  <span className={`badge ${evento.categoria.toLowerCase().replace('/', '-')}`}>{evento.categoria}</span>
                  <span className="impact" style={{ color: '#ef4444', fontWeight: 'bold' }}>ALERTA {evento.impacto}/5</span>
                </div>
                <h3>{evento.titulo}</h3>
                <p>{evento.resumo_analitico}</p>
              </div>
            ))}
            {highImpactEvents.length === 0 && <div className="text-center p-4 text-gray-500">Nenhum alerta crítico ativo.</div>}
          </>
        )}

        {activeTab === 'fontes' && (
          <div className="sources-panel p-2">
            <p className="text-sm text-gray-400 mb-4 text-center">Transparência de Inteligência</p>
            {sourcesCount.map(([fonte, count]) => (
              <div key={fonte} className="source-item">
                <span>{fonte}</span>
                <span className="source-count">{count} {count === 1 ? 'citação' : 'citações'}</span>
              </div>
            ))}
            {sourcesCount.length === 0 && <div className="text-center p-4 text-gray-500">Nenhuma fonte citada.</div>}
          </div>
        )}
      </div>
    </aside>
  );
};

export default React.memo(Sidebar);
