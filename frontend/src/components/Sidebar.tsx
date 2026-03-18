// © 2026 Pablo Dias. All rights reserved.
import React, { useMemo, useState } from 'react';
import { Shield, Globe, X, Filter, AlertTriangle, BookOpen, List } from 'lucide-react';
import { Event } from '../types';

interface SidebarProps {
  allEvents: Event[];
  events: Event[];
  onEventClick: (event: Event) => void;
  selectedCategory: string;
  setSelectedCategory: (category: string) => void;
  isOpen: boolean;
  toggleSidebar: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ 
  allEvents,
  events, 
  onEventClick, 
  selectedCategory, 
  setSelectedCategory, 
  isOpen, 
  toggleSidebar 
}) => {

  const [activeTab, setActiveTab] = useState<'feed' | 'alerts' | 'sources'>('feed');

  const militaryCount = useMemo(() => allEvents.filter(e => e.category.toLowerCase().includes('military')).length, [allEvents]);
  const highImpactEvents = useMemo(() => allEvents.filter(e => e.impact >= 4), [allEvents]);
  
  const sourcesCount = useMemo(() => {
    const counts: Record<string, number> = {};
    allEvents.forEach(e => {
      e.cited_sources.forEach(f => {
        counts[f] = (counts[f] || 0) + 1;
      });
    });
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
        <div 
          className="stat-card" 
          style={{ cursor: 'pointer' }}
          onClick={() => { setSelectedCategory('Military'); setActiveTab('feed'); }}
        >
          <Shield size={16} />
          <span>Military</span>
          <strong>{militaryCount}</strong>
        </div>
        <div 
          className="stat-card" 
          style={{ 
            cursor: 'pointer',
            borderColor: highImpactEvents.length > 0 ? '#ef4444' : 'transparent', 
            borderWidth: '1px', 
            borderStyle: 'solid' 
          }}
          onClick={() => setActiveTab('alerts')}
        >
          <AlertTriangle size={16} color={highImpactEvents.length > 0 ? '#ef4444' : 'currentColor'} />
          <span>Critical Alerts</span>
          <strong style={highImpactEvents.length > 0 ? { color: '#ef4444' } : {}}>{highImpactEvents.length}</strong>
        </div>
      </div>

      <div className="filter-section">
        <label><Filter size={14} /> Global Filter</label>
        <select 
          value={selectedCategory} 
          onChange={(e) => setSelectedCategory(e.target.value)}
          className="modern-select"
        >
          <option value="all">All Categories</option>
          <option value="Military">Military</option>
          <option value="Political">Political</option>
          <option value="Economic">Economic</option>
          <option value="Religious/Symbolic">Religious/Symbolic</option>
        </select>
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
                  <span className="impact">Impact: {event.impact}</span>
                </div>
                <h3>{event.title}</h3>
                <p>{event.analytical_summary.substring(0, 80)}...</p>
              </div>
            ))}
            {events.length === 0 && <div className="text-center p-4 text-gray-500">No events found.</div>}
          </>
        )}

        {activeTab === 'alerts' && (
          <>
            {highImpactEvents.map((event) => (
              <div key={event.id} className="feed-item" onClick={() => onEventClick(event)} style={{ borderColor: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.05)' }}>
                <div className="item-meta">
                  <span className={`badge ${getBadgeClass(event.category)}`}>{event.category}</span>
                  <span className="impact" style={{ color: '#ef4444', fontWeight: 'bold' }}>ALERT {event.impact}/5</span>
                </div>
                <h3>{event.title}</h3>
                <p>{event.analytical_summary}</p>
              </div>
            ))}
            {highImpactEvents.length === 0 && <div className="text-center p-4 text-gray-500">No active critical alerts.</div>}
          </>
        )}

        {activeTab === 'sources' && (
          <div className="sources-panel p-2">
            <p className="text-sm text-gray-400 mb-4 text-center">Intelligence Transparency</p>
            {sourcesCount.map(([source, count]) => (
              <div key={source} className="source-item">
                <span>{source}</span>
                <span className="source-count">{count} {count === 1 ? 'citation' : 'citations'}</span>
              </div>
            ))}
            {sourcesCount.length === 0 && <div className="text-center p-4 text-gray-500">No sources cited.</div>}
          </div>
        )}
      </div>
    </aside>
  );
};

export default React.memo(Sidebar);
