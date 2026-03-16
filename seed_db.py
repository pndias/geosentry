import random
from sqlalchemy.orm import Session
from src.api.database import SessionLocal, engine, Base
from src.api.models_db import EventoDB

# Garante que as tabelas existem
Base.metadata.create_all(bind=engine)

def generate_100_events():
    categorias = ['Militar', 'Politica', 'Economica', 'Religiosa/Simbólica']
    fontes = [
        "Relatórios OSINT local", "Agências Regionais", "Conselho Indígena", 
        "Mídia Independente", "Banco Central", "Movimentos Sociais", "Monitoramento via Satélite"
    ]
    
    # 10 Eventos base/âncoras focados no Sul Global
    base_events = [
        {"tit": "Escalada Naval", "res": "Movimentações marítimas atípicas bloqueiam rotas pesqueiras locais.", "lat_base": -1.0, "lon_base": -50.0},
        {"tit": "Tratado de Mineração", "res": "Novo acordo ameaça áreas de preservação ambiental e reservas hídricas.", "lat_base": -15.0, "lon_base": -60.0},
        {"tit": "Protestos Civis", "res": "Manifestações populares em resposta a medidas de austeridade severas.", "lat_base": -34.0, "lon_base": -58.0},
        {"tit": "Acordo Sul-Sul", "res": "Cooperação tecnológica entre nações em desenvolvimento para soberania de dados.", "lat_base": -23.0, "lon_base": 28.0},
        {"tit": "Conflito Fronteiriço", "res": "Atritos em região de fronteira deslocam milhares de camponeses.", "lat_base": 15.0, "lon_base": 30.0},
        {"tit": "Sancões Econômicas", "res": "Bloqueios externos afetam importação de medicamentos essenciais.", "lat_base": 5.0, "lon_base": -70.0},
        {"tit": "Cúpula Religiosa", "res": "Líderes de fé locais se unem para pedir paz e mediar conflito civil.", "lat_base": 10.0, "lon_base": 10.0},
        {"tit": "Apropriação de Terras", "res": "Corporações multinacionais iniciam expansão sobre terras comunais.", "lat_base": -5.0, "lon_base": 110.0},
        {"tit": "Nova Base Militar", "res": "Potência estrangeira instala infraestrutura militar no oceano pacífico.", "lat_base": 5.0, "lon_base": 130.0},
        {"tit": "Seca e Logística", "res": "Crise climática afeta canal logístico chave, encarecendo alimentos na região.", "lat_base": 20.0, "lon_base": -10.0}
    ]

    eventos = []
    for i in range(1, 101):
        base = random.choice(base_events)
        cat = random.choice(categorias)
        
        # Variação geográfica para espalhar os pontos pelo mapa
        lat_var = base["lat_base"] + random.uniform(-15.0, 15.0)
        lon_var = base["lon_base"] + random.uniform(-20.0, 20.0)
        
        # Clamp para coordenadas válidas
        lat_var = max(-90.0, min(90.0, lat_var))
        lon_var = max(-180.0, min(180.0, lon_var))

        eventos.append(
            EventoDB(
                titulo=f"{base['tit']} #{i}",
                categoria=cat,
                resumo_analitico=base["res"],
                lat=round(lat_var, 4),
                lon=round(lon_var, 4),
                impacto=random.randint(2, 5),
                tags=[cat.lower(), "sul-global"],
                fontes_citadas=random.sample(fontes, k=2),
                data=f"2026-03-{random.randint(1, 14):02d}",
                link_fonte=f"https://example.com/noticia/{i}"
            )
        )
    return eventos

def seed_database():
    db: Session = SessionLocal()
    
    # Recria a tabela para garantir as novas colunas
    print("Recriando tabelas...")
    EventoDB.__table__.drop(bind=engine, checkfirst=True)
    EventoDB.__table__.create(bind=engine)
    
    # Gera e insere
    print("Gerando 100 eventos geopolíticos focados no Sul Global...")
    eventos = generate_100_events()
    
    db.add_all(eventos)
    db.commit()
    print("Sucesso! Banco de dados local 'geosentry.db' populado com 100 eventos.")
    
    db.close()

if __name__ == "__main__":
    seed_database()
