// © 2026 Pablo Dias. All rights reserved.

import React, { useState, useCallback } from 'react';
import { Menu } from 'lucide-react';
import { useEvents } from './hooks/useEvents';
import { Event } from './types';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import EventMap from './components/EventMap';
import './index.css';

const App: React.FC = () => {
  const { events, filteredEvents, category, changeCategory, loading, error } = useEvents();
  
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(true);
  const [mapCenter, setMapCenter] = useState<[number, number]>([20, 0]);
  const [mapZoom, setMapZoom] = useState<number>(2);

  const handleEventClick = useCallback((event: Event) => {
    if (event.coordinates) {
      setMapCenter([event.coordinates.lat, event.coordinates.lon]);
      setMapZoom(5);
      
      if (window.innerWidth <= 768) {
        setSidebarOpen(false);
      }
    }
  }, []);

  const toggleSidebar = useCallback(() => setSidebarOpen(prev => !prev), []);

  return (
    <div className="dashboard-container">
      <button className="menu-toggle mobile-only" onClick={toggleSidebar}>
        <Menu />
      </button>

      <Sidebar 
        allEvents={events}
        events={filteredEvents} 
        onEventClick={handleEventClick}
        selectedCategory={category}
        setSelectedCategory={changeCategory}
        isOpen={sidebarOpen}
        toggleSidebar={toggleSidebar}
      />

      <main className="main-content">
        <Header />

        <div className="map-view">
          {error && <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-red-500 text-white px-4 py-2 rounded z-[1000]">{error}</div>}
          {loading && <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-blue-500 text-white px-4 py-2 rounded shadow-lg z-[1000]">Updating intelligence...</div>}
          
          <EventMap 
            events={filteredEvents} 
            mapCenter={mapCenter} 
            mapZoom={mapZoom} 
          />
        </div>
      </main>
    </div>
  );
};

export default App;
