# BidMind

Zambian procurement intelligence platform. Monitors 7 government and private tender portals, extracts structured data via AI, and alerts suppliers via WhatsApp.

## Portals Monitored

1. **ZPPA** (eprocure.zppa.org.zm) — Government, 133,000+ tenders
2. **ZESCO** (zesco.co.zm) — Energy parastatal
3. **UNGM** (ungm.org) — UN procurement, Zambia filtered
4. **Bank of Zambia** (boz.zm) — Central bank tenders
5. **RDA** (rda.org.zm) — Road Development Agency
6. **KoBold Metals** (koboldmetals.com/partner-zambia) — Private mining
7. **ZCCM-IH** (zccm-ih.com.zm/procurement) — State mining investments

## Features

- **Multi-source scraping** — All 7 portals via async scrapers
- **AI extraction** — Gemini, OpenAI, or Claude for structured data
- **WhatsApp alerts** — Instant notifications on keyword matches
- **Admin dashboard** — Real-time monitoring API
- **Scheduler** — Runs every 4 hours via APScheduler

## Quick Start

source .venv/bin/activate
alembic upgrade head
python -c "from app.scraper.manager import ScraperManager; import asyncio; asyncio.run(ScraperManager().run_all())"
uvicorn main:app --reload

## Project Structure

bidmind/
├── app/
│   ├── api/v1/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── scraper/
│   ├── tasks/
│   └── core/
├── alembic/
├── tests/
├── .env
├── requirements.txt
└── README.md

## License

MIT

## Author

Mahmoud
