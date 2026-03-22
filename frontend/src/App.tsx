// © 2026 Pablo Dias. All rights reserved.

import React, { useState, useCallback, useEffect } from 'react';
import { Menu } from 'lucide-react';
import { useEvents } from './hooks/useEvents';
import { Event } from './types';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import EventMap from './components/EventMap';
import './index.css';

const App: React.FC = () => {
  const { events, filteredEvents, category, context, changeCategory, changeContext, loading, error, userLocation, fetchNearby } = useEvents();
  
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(false);
  const [mapCenter, setMapCenter] = useState<[number, number]>([20, 0]);
  const [mapZoom, setMapZoom] = useState<number>(8);

  useEffect(() => {
    if (userLocation) {
      setMapCenter(userLocation);
      setMapZoom(8);
    }
  }, [userLocation]);

  const handleEventClick = useCallback((event: Event) => {
    if (event.coordinates) {
      setMapCenter([event.coordinates.lat, event.coordinates.lon]);
      setMapZoom(8);
      if (window.innerWidth <= 768) setSidebarOpen(false);
    }
  }, []);

  const toggleSidebar = useCallback(() => setSidebarOpen(prev => !prev), []);

  return (
    <div className="dashboard-container">
      <button className="menu-toggle" onClick={toggleSidebar} aria-label="Toggle menu">
        <Menu size={20} />
      </button>

      {sidebarOpen && <div className="sidebar-overlay" onClick={toggleSidebar} />}

      <Sidebar 
        allEvents={events}
        events={filteredEvents} 
        onEventClick={handleEventClick}
        selectedCategory={category}
        setSelectedCategory={changeCategory}
        selectedContext={context}
        setSelectedContext={changeContext}
        isOpen={sidebarOpen}
        toggleSidebar={toggleSidebar}
      />

      <main className="main-content">
        <Header />
        <div className="map-view">
          {error && <div className="toast toast-error">{error}</div>}
          {loading && <div className="toast toast-info">Updating intelligence...</div>}
          <EventMap 
            events={filteredEvents} 
            mapCenter={mapCenter} 
            mapZoom={mapZoom}
            onViewChange={fetchNearby}
          />
        </div>
      </main>
    </div>
  );
};

export default App;
