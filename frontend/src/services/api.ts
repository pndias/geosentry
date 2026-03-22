import { Event } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api';
const FALLBACK_URL = 'http://localhost:8000';

async function apiFetch(path: string): Promise<Event[]> {
  try {
    const res = await fetch(`${API_BASE_URL}${path}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch {
    const res = await fetch(`${FALLBACK_URL}${path}`);
    if (!res.ok) throw new Error(`Fallback HTTP ${res.status}`);
    return await res.json();
  }
}

export const eventService = {
  fetchEvents: (context?: string) => {
    const params = context ? `?context=${encodeURIComponent(context)}` : '';
    return apiFetch(`/events${params}`);
  },
  fetchNearby: (lat: number, lon: number, radiusKm = 2000) =>
    apiFetch(`/events/nearby?lat=${lat}&lon=${lon}&radius_km=${radiusKm}`),
};
