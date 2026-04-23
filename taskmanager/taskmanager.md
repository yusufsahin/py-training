# Proje Spesifikasyonu: Basit Task Yönetimi Uygulaması (MVP)

Bu döküman, projenin teknik mimarisini, veri modelini ve geliştirme yol haritasını içerir. AI kod asistanları (Cursor, Windsurf vb.) için ana referans kaynağıdır.

## 1. Proje Özeti
Kullanıcıların projeler oluşturabildiği, bu projeler içinde görevleri (task) Kanban board veya liste şeklinde yönetebildiği, önceliklendirme ve durum takibi yapabildiği bir MVP.

## 2. Teknoloji Stack
- **Frontend:** React 19 (Vite ile), TypeScript
- **Styling:** Tailwind CSS + shadcn/ui
- **State Management:** Zustand (Global UI state), TanStack Query (Server state/Caching)
- **Backend/DB:** Supabase (PostgreSQL, Auth, Storage)
- **Drag & Drop:** @dnd-kit/core (Kanban için)
- **Icons:** Lucide React

## 3. Veri Modeli (Database Schema)

### 3.1. profiles (Kullanıcılar)
- `id`: uuid (PK, references auth.users)
- `full_name`: text
- `email`: text
- `avatar_url`: text

### 3.2. projects (Projeler)
- `id`: uuid (PK, default: uuid_generate_v4())
- `name`: text (not null)
- `owner_id`: uuid (FK -> profiles.id)
- `created_at`: timestamptz (default: now())

### 3.3. tasks (Görevler)
- `id`: uuid (PK)
- `project_id`: uuid (FK -> projects.id)
- `title`: text (not null)
- `description`: text
- `status`: enum ('todo', 'in_progress', 'done')
- `priority`: enum ('low', 'medium', 'high')
- `due_date`: timestamptz
- `position`: float (manuel sıralama/kanban için)
- `is_deleted`: boolean (default: false)
- `created_at`: timestamptz

### 3.4. labels (Etiketler)
- `id`: uuid
- `name`: text
- `color`: text (hex code)

### 3.5. task_labels (Çoka-Çok İlişki)
- `task_id`: uuid (FK)
- `label_id`: uuid (FK)

## 4. Klasör Yapısı (Folder Structure)
```text
src/
├── api/              # Supabase client ve query fetcher'lar
├── components/
│   ├── ui/           # shadcn/ui bileşenleri
│   ├── layout/       # Navbar, Sidebar, Page Wrapper
│   └── shared/       # Reusable bileşenler (StatusBadge, PriorityIcon)
├── features/         # Özellik bazlı gruplandırma
│   ├── auth/         # Login/Register logic
│   ├── projects/     # Proje listesi ve CRUD
│   └── tasks/        # KanbanBoard, TaskCard, TaskModal, TaskFilters
├── hooks/            # Custom hooks (useTasks, useProjects)
├── store/            # Zustand store tanımları
└── types/            # TypeScript interface ve type tanımları