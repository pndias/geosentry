// © 2026 Pablo Dias. All rights reserved.
import React, { useMemo, useState } from 'react';
import { Shield, Globe, X, Filter, AlertTriangle, BookOpen, List, Flame } from 'lucide-react';
import { Event, EventContext } from '../types';

interface SidebarProps {
  allEvents: Event[];
  events: Event[];
  onEventClick: (event: Event) => void;
  selectedCategory: string;
  setSelectedCategory: (category: string) => void;
  selectedContext: EventContext | 'all';
  setSelectedContext: (context: EventContext | 'all') => void;
  isOpen: boolean;
  toggleSidebar: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ 
  allEvents, events, onEventClick, 
  selectedCategory, setSelectedCategory,
  selectedContext, setSelectedContext,
  isOpen, toggleSidebar,
}) => {
  const [activeTab, setActiveTab] = useState<'feed' | 'alerts' | 'sources'>('feed');

  const militaryCount = useMemo(() => allEvents.filter(e => e.category.toLowerCase().includes('military')).length, [allEvents]);
  const globalThreatsCount = useMemo(() => allEvents.filter(e => e.context === 'Global Threats').length, [allEvents]);
  const highImpactEvents = useMemo(() => allEvents.filter(e => e.impact >= 4), [allEvents]);
  
  const sourcesCount = useMemo(() => {
    const counts: Record<string, number> = {};
    allEvents.forEach(e => e.cited_sources.forEach(f => { counts[f] = (counts[f] || 0) + 1; }));
    return Object.entries(counts).sort((a, b) => b[1] - a[1]);
  }, [allEvents]);

  const getBadgeClass = (category: string) => {
    const norm = category.toLowerCase();
    if (norm.includes('military')) return 'military';
    if (norm.includes('political')) return 'political';
    if (norm.includes('economic')) return 'economic';
    if (norm.includes('religious') || norm.includes('symbolic')) return 'religious-symbolic';
    return '';
  };

  const getContextBadge = (ctx: string) => {
    if (ctx === 'Global Threats') return 'global-threats';
    return 'regional';
  };

  return (
    <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
      <div className="sidebar-header">
        <div className="logo">
          <Globe size={28} className="text-blue-500" />
          <span>GeoSentry</span>
        </div>
        <button className="close-btn" onClick={toggleSidebar} aria-label="Close sidebar"><X size={20} /></button>
      </div>

      <div className="stats-grid">
        <div className="stat-card" style={{ cursor: 'pointer' }}
          onClick={() => { setSelectedCategory('Military'); setSelectedContext('all'); setActiveTab('feed'); }}>
          <Shield size={16} />
          <span>Military</span>
          <strong>{militaryCount}</strong>
        </div>
        <div className="stat-card" style={{ cursor: 'pointer', borderColor: globalThreatsCount > 0 ? '#f97316' : 'transparent', borderWidth: '1px', borderStyle: 'solid' }}
          onClick={() => { setSelectedContext('Global Threats'); setSelectedCategory('all'); setActiveTab('feed'); }}>
          <Flame size={16} color={globalThreatsCount > 0 ? '#f97316' : 'currentColor'} />
          <span>Global Threats</span>
          <strong style={globalThreatsCount > 0 ? { color: '#f97316' } : {}}>{globalThreatsCount}</strong>
        </div>
        <div className="stat-card" style={{ cursor: 'pointer', borderColor: highImpactEvents.length > 0 ? '#ef4444' : 'transparent', borderWidth: '1px', borderStyle: 'solid' }}
          onClick={() => setActiveTab('alerts')}>
          <AlertTriangle size={16} color={highImpactEvents.length > 0 ? '#ef4444' : 'currentColor'} />
          <span>Critical Alerts</span>
          <strong style={highImpactEvents.length > 0 ? { color: '#ef4444' } : {}}>{highImpactEvents.length}</strong>
        </div>
        <div className="stat-card" style={{ cursor: 'pointer' }}
          onClick={() => { setSelectedContext('Regional'); setSelectedCategory('all'); setActiveTab('feed'); }}>
          <Globe size={16} />
          <span>Regional</span>
          <strong>{allEvents.filter(e => e.context === 'Regional').length}</strong>
        </div>
      </div>

      <div className="filter-section">
        <div className="filter-row">
          <label><Filter size={14} /> Context</label>
          <select value={selectedContext} onChange={(e) => setSelectedContext(e.target.value as EventContext | 'all')} className="modern-select">
            <option value="all">All Contexts</option>
            <option value="Global Threats">Global Threats</option>
            <option value="Regional">Regional</option>
          </select>
        </div>
        <div className="filter-row">
          <label><Filter size={14} /> Category</label>
          <select value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)} className="modern-select">
            <option value="all">All Categories</option>
            <option value="Military">Military</option>
            <option value="Political">Political</option>
            <option value="Economic">Economic</option>
            <option value="Religious/Symbolic">Religious/Symbolic</option>
          </select>
        </div>
      </div>

      <div className="sidebar-tabs">
        <button className={`tab-btn ${activeTab === 'feed' ? 'active' : ''}`} onClick={() => setActiveTab('feed')}><List size={14}/> Feed</button>
        <button className={`tab-btn ${activeTab === 'alerts' ? 'active' : ''}`} onClick={() => setActiveTab('alerts')}><AlertTriangle size={14}/> Alerts</button>
        <button className={`tab-btn ${activeTab === 'sources' ? 'active' : ''}`} onClick={() => setActiveTab('sources')}><BookOpen size={14}/> Sources</button>
      </div>

      <div className="event-feed">
        {activeTab === 'feed' && (
          <>
            {events.map((event) => (
              <div key={event.id} className="feed-item" onClick={() => onEventClick(event)}>
                <div className="item-meta">
                  <span className={`badge ${getBadgeClass(event.category)}`}>{event.category}</span>
                  <span className={`badge ${getContextBadge(event.context)}`}>{event.context}</span>
                  <span className="impact">Impact: {event.impact}</span>
                </div>
                <h3>{event.title}</h3>
                <p>{event.analytical_summary.substring(0, 80)}...</p>
              </div>
            ))}
            {events.length === 0 && <div className="empty-state">No events found.</div>}
          </>
        )}

        {activeTab === 'alerts' && (
          <>
            {highImpactEvents.map((event) => (
              <div key={event.id} className="feed-item feed-item-alert" onClick={() => onEventClick(event)}>
                <div className="item-meta">
                  <span className={`badge ${getBadgeClass(event.category)}`}>{event.category}</span>
                  <span className={`badge ${getContextBadge(event.context)}`}>{event.context}</span>
                  <span className="impact" style={{ color: '#ef4444', fontWeight: 'bold' }}>ALERT {event.impact}/5</span>
                </div>
                <h3>{event.title}</h3>
                <p>{event.analytical_summary}</p>
              </div>
            ))}
            {highImpactEvents.length === 0 && <div className="empty-state">No active critical alerts.</div>}
          </>
        )}

        {activeTab === 'sources' && (
          <div className="sources-panel">
            <p className="sources-title">Intelligence Transparency</p>
            {sourcesCount.map(([source, count]) => (
              <div key={source} className="source-item">
                <span>{source}</span>
                <span className="source-count">{count} {count === 1 ? 'citation' : 'citations'}</span>
              </div>
            ))}
            {sourcesCount.length === 0 && <div className="empty-state">No sources cited.</div>}
          </div>
        )}
      </div>
    </aside>
  );
};

export default React.memo(Sidebar);
