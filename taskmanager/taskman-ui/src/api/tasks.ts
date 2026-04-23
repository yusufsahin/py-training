import { apiJson } from './client';
import type { Task, TaskPriority, TaskStatus } from '../types';

export interface TaskCreatePayload {
  project_id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  due_date?: string;
  position: number;
  label_ids?: string[];
}

export interface TaskUpdatePayload {
  title?: string;
  description?: string | null;
  status?: TaskStatus;
  priority?: TaskPriority;
  due_date?: string | null;
  position?: number;
  is_deleted?: boolean;
  label_ids?: string[];
}

export async function listTasks(projectId: string): Promise<Task[]> {
  const q = new URLSearchParams({ project_id: projectId });
  return apiJson<Task[]>(`/tasks?${q.toString()}`);
}

export async function createTask(payload: TaskCreatePayload): Promise<Task> {
  return apiJson<Task>('/tasks', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export async function patchTask(id: string, payload: TaskUpdatePayload): Promise<Task> {
  return apiJson<Task>(`/tasks/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  });
}
