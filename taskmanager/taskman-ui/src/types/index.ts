export type TaskStatus = 'todo' | 'in_progress' | 'done';
export type TaskPriority = 'low' | 'medium' | 'high';

export interface Profile {
  id: string;
  full_name: string;
  email: string;
  avatar_url?: string;
}

export interface Project {
  id: string;
  name: string;
  owner_id: string;
  created_at: string;
}

export interface Task {
  id: string;
  project_id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  due_date?: string;
  position: number;
  is_deleted: boolean;
  created_at: string;
  labels: Label[];
}

export interface Label {
  id: string;
  name: string;
  color: string;
}
