export type Category = 'Military' | 'Political' | 'Economic' | 'Religious/Symbolic';

export interface Coordinates {
  lat: number;
  lon: number;
}

export interface Event {
  id: number;
  title: string;
  category: Category;
  analytical_summary: string;
  coordinates?: Coordinates;
  impact: number;
  cited_sources: string[];
  tags: string[];
  source_link?: string;
}
