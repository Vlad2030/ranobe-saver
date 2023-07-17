# RanobeSaver

Service for download your best ranobes for free from ranobelib.me

## Roadmap
 - [ ] Backend
    - [ ] Create project arch
    - [ ] /users
        - [ ] Endpoints
        - [ ] CRUD
        - [ ] DB models
        - [ ] Schemas
    - [ ] /ranobes
        - [ ] Endpoints
        - [ ] CRUD
        - [ ] DB models
        - [ ] Schemas
    - [ ] Docker
        - [ ] Dockerfile
    - [ ] .env
 - [ ] Telegram Bot
    - [ ] Create project arch
    - [ ] Requests with backend
    - [ ] Celery broker
    - [ ] Message handlers
        - [ ] /start
        - [ ] /ranobe
        - [ ] /help
    - [ ] Callback handlers
        - [ ] ...
        - [ ] ...
        - [ ] ...
    - [ ] Inline mode
    - [ ] Ad and news mailing
    - [ ] Ranobe events
    - [ ] Docker
        - [ ] Dockerfile
    - [ ] .env
 - [ ] Docker-compose
 - [ ] Release MVP

## Stack
### Backend:
 - Python 3.10 (FastAPI, SQLAIchemy, Aiohttp)
 - Docker
![](https://img.shields.io/badge/Python-316192?style=for-the-badge&logo=python&logoColor=white&color=3776AB)
![](https://img.shields.io/badge/fastapi-316192?style=for-the-badge&logo=fastapi&logoColor=white&color=009688)
![](https://img.shields.io/badge/AIOHTTP-316192?style=for-the-badge&logo=aiohttp&logoColor=white&color=2C5BB4)
![](https://img.shields.io/badge/Docker-316192?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)

### Telegram Bot:
 - Python 3.10 (Aiogram 3.0, Aiohttp)
 - Docker
![](https://img.shields.io/badge/Python-316192?style=for-the-badge&logo=python&logoColor=white&color=3776AB)
![](https://img.shields.io/badge/AIOHTTP-316192?style=for-the-badge&logo=aiohttp&logoColor=white&color=2C5BB4)
![](https://img.shields.io/badge/Docker-316192?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)

## Dependencies
### Telegram bot:
 - aiogram>=3.0.0b7
 - aiohttp==3.8.4
 - loguru>=0.6.0
 - orjson>=3.8.8
 - python-dotenv==1.0.0

### Backend:
 - aiohttp==3.8.4
 - alembic==1.10.3
 - asyncio==3.4.3
 - asyncpg==0.27.0
 - fastapi==0.95.1
 - gunicorn==20.1.0
 - loguru==0.6.0
 - orjson==3.8.10
 - pydantic==1.10.7
 - python-dotenv==1.0.0
 - SQLAlchemy==2.0.9
 - uvicorn==0.21.1
