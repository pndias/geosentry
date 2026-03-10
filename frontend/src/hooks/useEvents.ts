import { useState, useEffect, useMemo, useCallback } from 'react';
import { Evento } from '../types';
import { eventoService } from '../services/api';

export const useEvents = () => {
  const [events, setEvents] = useState<Evento[]>([]);
  const [category, setCategory] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadEvents = async () => {
      try {
        setLoading(true);
        const data = await eventoService.fetchEventos();
        setEvents(data);
        setError(null);
      } catch (err: any) {
        setError(err.message || 'Erro ao buscar eventos');
      } finally {
        setLoading(false);
      }
    };

    loadEvents();
  }, []);

  const filteredEvents = useMemo(() => {
    if (category === 'all') return events;
    return events.filter(e => e.categoria === category);
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
