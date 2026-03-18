import { Event } from '../types';

const API_BASE_URL = '/api';

export const eventService = {
  fetchEvents: async (): Promise<Event[]> => {
    try {
      const response = await fetch(`${API_BASE_URL}/events`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.warn("Proxy fetch failed, falling back to localhost:8000", error);
      const fallbackResponse = await fetch('http://localhost:8000/events');
      if (!fallbackResponse.ok) {
        throw new Error(`Fallback HTTP error! status: ${fallbackResponse.status}`);
      }
      return await fallbackResponse.json();
    }
  }
};
