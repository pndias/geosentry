import random
from sqlalchemy.orm import Session
from src.infrastructure.database.session import SessionLocal, engine, Base
from src.infrastructure.database.models import EventDB

# Ensure tables exist
Base.metadata.create_all(bind=engine)

def generate_500_events():
    categories = ['Military', 'Political', 'Economic', 'Religious/Symbolic']
    sources = [
        "Local OSINT Reports", "Regional Agencies", "Indigenous Council",
        "Independent Media", "Central Bank", "Social Movements", "Satellite Monitoring",
        "Reuters", "Associated Press", "Al Jazeera", "Conflict Observatory"
    ]
    
    # Base/anchor events including Global South, USA, and Europe
    base_events = [
        {"tit": "Naval Escalation", "sum": "Atypical maritime movements blocking local fishing routes.", "lat_base": -1.0, "lon_base": -50.0},
        {"tit": "Mining Treaty", "sum": "New agreement threatens environmental preservation areas and water reserves.", "lat_base": -15.0, "lon_base": -60.0},
        {"tit": "Civil Protests", "sum": "Popular demonstrations in response to severe austerity measures.", "lat_base": -34.0, "lon_base": -58.0},
        {"tit": "South-South Agreement", "sum": "Technological cooperation between developing nations for data sovereignty.", "lat_base": -23.0, "lon_base": 28.0},
        {"tit": "Border Conflict", "sum": "Friction in border region displaces thousands of peasants.", "lat_base": 15.0, "lon_base": 30.0},
        {"tit": "Economic Sanctions", "sum": "External blockades affect importation of essential medicines.", "lat_base": 5.0, "lon_base": -70.0},
        {"tit": "Religious Summit", "sum": "Local faith leaders unite to call for peace and mediate civil conflict.", "lat_base": 10.0, "lon_base": 10.0},
        {"tit": "Land Grabbing", "sum": "Multinational corporations begin expansion over communal lands.", "lat_base": -5.0, "lon_base": 110.0},
        {"tit": "New Military Base", "sum": "Foreign power installs military infrastructure in the Pacific Ocean.", "lat_base": 5.0, "lon_base": 130.0},
        {"tit": "Drought and Logistics", "sum": "Climate crisis affects key logistics channel, raising food prices in the region.", "lat_base": 20.0, "lon_base": -10.0},
        # USA and Europe
        {"tit": "European Parliament Resolution", "sum": "European parliament decision imposes new tariff barriers on southern countries.", "lat_base": 50.8, "lon_base": 4.3},
        {"tit": "NATO Troop Movement", "sum": "Large-scale military exercises on the eastern European border raise global tensions.", "lat_base": 52.2, "lon_base": 21.0},
        {"tit": "Federal Reserve Decision", "sum": "US interest rate hike causes capital flight from emerging countries.", "lat_base": 38.9, "lon_base": -77.0},
        {"tit": "Bilateral Sanctions (USA)", "sum": "Direct sanctions applied by the US Treasury block access to essential semiconductors.", "lat_base": 38.9, "lon_base": -77.0},
        {"tit": "Climate Protests (EU)", "sum": "Internal pressure in Europe forcing governments to externalize environmental costs.", "lat_base": 48.8, "lon_base": 2.3}
    ]

    events = []
    for i in range(1, 501):
        base = random.choice(base_events)
        cat = random.choice(categories)
        
        lat_var = base["lat_base"] + random.uniform(-10.0, 10.0)
        lon_var = base["lon_base"] + random.uniform(-15.0, 15.0)
        
        lat_var = max(-90.0, min(90.0, lat_var))
        lon_var = max(-180.0, min(180.0, lon_var))

        events.append(
            EventDB(
                title=f"{base['tit']} #{i}",
                category=cat,
                analytical_summary=base["sum"],
                lat=round(lat_var, 4),
                lon=round(lon_var, 4),
                impact=random.randint(2, 5),
                tags=[cat.lower(), "global-south", "geopolitics"],
                cited_sources=random.sample(sources, k=2),
                date=f"2026-03-{random.randint(1, 16):02d}",
                source_link=f"https://example.com/news/{i}"
            )
        )
    return events

def seed_database():
    db: Session = SessionLocal()
    
    print("Recreating tables...")
    EventDB.__table__.drop(bind=engine, checkfirst=True)
    EventDB.__table__.create(bind=engine)
    
    print("Generating 500 geopolitical events...")
    events = generate_500_events()
    
    db.add_all(events)
    db.commit()
    print("Success! Local database 'geosentry.db' populated with 500 events.")
    
    db.close()

if __name__ == "__main__":
    seed_database()
