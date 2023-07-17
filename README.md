![](https://github.com/Vlad2030/ranobe-saver/assets/61238982/f71e1d10-e222-4e8d-bb8c-4fe74e8707ac)

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
![](https://img.shields.io/badge/Python-316192?style=for-the-badge&logo=python&logoColor=white&color=3776AB)
![](https://img.shields.io/badge/fastapi-316192?style=for-the-badge&logo=fastapi&logoColor=white&color=009688)
![](https://img.shields.io/badge/AIOHTTP-316192?style=for-the-badge&logo=aiohttp&logoColor=white&color=2C5BB4)
![](https://img.shields.io/badge/Docker-316192?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)

 - Python 3.10 (FastAPI, SQLAIchemy, Aiohttp)
 - Docker


### Telegram Bot:
![](https://img.shields.io/badge/Python-316192?style=for-the-badge&logo=python&logoColor=white&color=3776AB)
![](https://img.shields.io/badge/AIOHTTP-316192?style=for-the-badge&logo=aiohttp&logoColor=white&color=2C5BB4)
![](https://img.shields.io/badge/Docker-316192?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)

 - Python 3.10 (Aiogram 3.0, Aiohttp)
 - Docker


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

## Backend
REST API docs

### `/users` endpoint

#### **POST** /users/
Create a new user

*request body*
```json
{
    "user_id": "1840037832",
    "username": "vladdd00",
    "full_name": "влад",
    "admin": true
}
```

*response body*
```json
{
    "created": true,
}
```

---

#### **PATCH** /users/{id}/
User edit

*request body*
```json
{
    "admin": false (or null)
}
```

> P.S. if the value is `null` it will not be changed


*response body*
```json
{
    "success": true,
}
```
---

#### **GET** /users/
Get users list

*query parameters*
```json
{
    "limit": 1 (optional, default=50) 
}
```

*response body*
```json
{
    "users": [
        {
            "id": 1,
            "telegram": {
                "user_id": "1840037832",
                "username": "vladdd00",
                "full_name": "влад",
            },
            "admin": true
        }
    ]
}
```

---

#### **GET** /users/count/
Get users count

*response body*
```json
{
    "count": 1,
    "admin_count": 1
}
```

---

#### **GET** /users/{id}/
Get user by id

*response body*
```json
{
    "id": 1,
    "telegram": {
        "user_id": "1840037832",
        "username": "vladdd00",
        "full_name": "влад",
    },
    "admin": true
}
```

---

### `/telegram` endpoint

#### **GET** /telegram/users/{user_id}/
Get telegram user by user_id

*response body*
```json
{
    "user_id": "1840037832",
    "username": "vladdd00",
    "full_name": "влад",
    "admin": true
}
```

---

### `/ranobes` endpoint
> in development
