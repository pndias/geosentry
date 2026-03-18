import { useState, useEffect, useMemo, useCallback } from 'react';
import { Event } from '../types';
import { eventService } from '../services/api';

export const useEvents = () => {
  const [events, setEvents] = useState<Event[]>([]);
  const [category, setCategory] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [userLocation, setUserLocation] = useState<[number, number] | null>(null);

  const fetchNearby = useCallback(async (lat: number, lon: number, radiusKm: number) => {
    try {
      setLoading(true);
      const data = await eventService.fetchNearby(lat, lon, radiusKm);
      setEvents(data);
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Error fetching events');
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchAll = useCallback(async () => {
    try {
      setLoading(true);
      const data = await eventService.fetchEvents();
      setEvents(data);
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Error fetching events');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const loc: [number, number] = [pos.coords.latitude, pos.coords.longitude];
          setUserLocation(loc);
          fetchNearby(loc[0], loc[1], 2000);
        },
        () => fetchAll(),
        { timeout: 5000 },
      );
    } else {
      fetchAll();
    }
  }, [fetchNearby, fetchAll]);

  const filteredEvents = useMemo(() => {
    if (category === 'all') return events;
    return events.filter(e => e.category.toLowerCase().includes(category.toLowerCase()));
  }, [events, category]);

  const changeCategory = useCallback((newCategory: string) => {
    setCategory(newCategory);
  }, []);

  return {
    events,
    filteredEvents,
    category,
    changeCategory,
    loading,
    error,
    userLocation,
    fetchNearby,
  };
};
