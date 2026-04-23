# taskman-api

FastAPI backend for TaskFlow: PostgreSQL, JWT auth, projects, tasks, labels.

## Prerequisites

- Python 3.11+
- Docker (optional, for PostgreSQL)

## Configuration

Copy `.env.example` to `.env` and adjust values.

- `DATABASE_URL` — SQLAlchemy URL, e.g. `postgresql+psycopg://taskman:taskman@localhost:5432/taskman`
- `JWT_SECRET` — long random string for signing tokens
- `CORS_ORIGINS` — comma-separated browser origins (e.g. `http://localhost:5173`)

## Run PostgreSQL

From this directory:

```bash
docker compose up -d
```

## Install and migrate

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
```

## Run the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- OpenAPI: `http://localhost:8000/docs`
- Health: `GET http://localhost:8000/health`

## API overview

- `POST /auth/register` — body: `email`, `password`, `full_name`; returns JWT and seeds default labels
- `POST /auth/login` — body: `email`, `password`
- `GET /auth/me` — requires `Authorization: Bearer <token>`
- `GET/POST /projects`, `DELETE /projects/{id}`
- `GET /tasks?project_id=<uuid>`, `POST /tasks`, `PATCH /tasks/{id}`
- `GET /labels`

## Manual smoke test

1. Register a user, then `GET /auth/me` with the token.
2. Create a project, list tasks (empty), create a task, patch status to `done`.
3. Refresh list; data should persist in Postgres.
