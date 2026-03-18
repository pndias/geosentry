import { useState, useEffect, useMemo, useCallback } from 'react';
import { Event } from '../types';
import { eventService } from '../services/api';

export const useEvents = () => {
  const [events, setEvents] = useState<Event[]>([]);
  const [category, setCategory] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadEvents = async () => {
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
    };

    loadEvents();
  }, []);

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
    error
  };
};
