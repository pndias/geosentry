# GeoSentry — Session Context (2026-03-22)

## Branch: `realtest`

## What was done this session

### 1. Cloudflare Domain Setup (planned, not yet applied to code)
- Domain: `geosentry.app` (bought through Cloudflare Registrar — nameservers auto-configured)
- Plan: Use **Cloudflare Tunnel** (`cloudflared`) to expose local services through the domain
- Steps 1–4 (Cloudflare dashboard config) discussed; Steps 5–8 (nginx SSL, docker-compose changes) NOT yet applied
- No server purchased — running locally through tunnel is the chosen approach

### 2. GLOBAL THREATS Context Filter (implemented)
New `EventContext` enum: `Regional` | `Global Threats`

**Classification criteria** (in `seed_db.py` → `_is_global_threat()`):
- Impact >= 5
- Tags match: nato, brics, un, eu, mercosur, wef, war, trade-war, naval-blockade, oil-shock, intervention, oil, energy, hormuz
- Title keywords: nato, brics, un, strait of hormuz, trade war, emergency tariff, oil shock, intervention, iran, section 301, cbam

**Files changed (backend):**
- `src/domain/entities.py` — `EventContext` enum + `context` field on `GeopoliticalEvent`
- `src/domain/repositories.py` — `list_by_context()` abstract method
- `src/infrastructure/database/models.py` — `context` column (indexed)
- `src/infrastructure/database/repositories.py` — `list_by_context()` impl
- `src/application/services/event_service.py` — `list_by_context()` service method
- `src/api/routers/eventos.py` — `?context=` query param on `GET /events`
- `seed_db.py` — `_is_global_threat()` classifier + `context` field in seed data

**API:**
```
GET /events                          → all events
GET /events?context=Global Threats   → only global threats
GET /events?context=Regional         → only regional
```

### 3. Frontend Adaptive/Responsive Redesign (implemented)
**Files changed:**
- `frontend/src/types/index.ts` — `EventContext` type + `context` on `Event`
- `frontend/src/services/api.ts` — `fetchEvents(context?)` support
- `frontend/src/hooks/useEvents.ts` — dual filter state (context + category)
- `frontend/src/App.tsx` — hamburger menu, overlay sidebar, context props
- `frontend/src/components/Sidebar.tsx` — 4 stat cards (Military, Global Threats, Critical Alerts, Regional), 2 filter dropdowns (Context + Category), context badges
- `frontend/src/components/EventMap.tsx` — Global Threat badge in map popups
- `frontend/src/index.css` — full responsive rewrite: slide-out sidebar, mobile overlay at 85vw, desktop push layout

### 4. Startup Scripts Fixed
- `start.sh` — seeds DB **before** starting API (was wrong order before)
- `run-macos.sh` — shows global threats count in startup summary

## Next steps
- [ ] Set up Cloudflare Tunnel (`cloudflared`) to expose local Docker services through `geosentry.app`
- [ ] Update `nginx.conf` for SSL with Cloudflare Origin Certificate
- [ ] Update `docker-compose-swarm.yml` to mount certs and expose port 443
- [ ] Update `frontend.Dockerfile` to copy certs
- [ ] Add `geosentry.app` to CORS allowed origins in `src/api/main.py`
- [ ] Test full stack locally with `./start.sh` or `./run-macos.sh`
