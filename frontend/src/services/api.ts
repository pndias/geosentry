import { Evento } from '../types';

const API_BASE_URL = '/api';

export const eventoService = {
  fetchEventos: async (): Promise<Evento[]> => {
    try {
      const response = await fetch(`${API_BASE_URL}/eventos`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.warn("Proxy fetch failed, falling back to localhost:8000", error);
      // Fallback para desenvolvimento local caso o proxy falhe
      const fallbackResponse = await fetch('http://localhost:8000/eventos');
      if (!fallbackResponse.ok) {
        throw new Error(`Fallback HTTP error! status: ${fallbackResponse.status}`);
      }
      return await fallbackResponse.json();
    }
  }
};
