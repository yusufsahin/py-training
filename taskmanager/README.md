# Taskmanager (TaskFlow MVP)

Full-stack task board: **taskman-api** (FastAPI + PostgreSQL + JWT) and **taskman-ui** (Vite + React + TanStack Query + Zustand UI state).

## Quick start

### 1. Database and API

```bash
cd taskman-api
copy .env.example .env
docker compose up -d
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend

In a second terminal:

```bash
cd taskman-ui
copy .env.example .env
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`). Register, create a project, add tasks, use Kanban or list view.

## Environment

| Location | Variable | Purpose |
|----------|----------|---------|
| taskman-api `.env` | `DATABASE_URL`, `JWT_SECRET`, `CORS_ORIGINS` | API and database |
| taskman-ui `.env` | `VITE_API_BASE_URL` | API base URL (default `http://localhost:8000`) |

`CORS_ORIGINS` must include the UI origin (e.g. `http://localhost:5173`).

## Product spec

See [taskmanager.md](taskmanager.md) for the original data model and UX goals.

## Manual E2E checklist

1. Register a new account; confirm redirect to the main shell.
2. Create a project; it appears in the sidebar and is selected.
3. Add a task; it appears in Kanban and list modes.
4. Drag a task to another column; status updates after refresh.
5. Soft-delete a task from the card menu; it disappears from the board.
6. Log out and log back in; projects and tasks still load from the API.
