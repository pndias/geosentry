export type Categoria = 'Militar' | 'Politica' | 'Economica' | 'Religiosa/Simbólica';

export interface Coordenadas {
  lat: number;
  lon: number;
}

export interface Evento {
  id: number;
  titulo: string;
  categoria: Categoria;
  resumo_analitico: string;
  coordenadas?: Coordenadas;
  impacto: number;
  fontes_citadas: string[];
  tags: string[];
  link_fonte?: string;
}
