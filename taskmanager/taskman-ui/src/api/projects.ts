import { apiJson } from './client';
import type { Project } from '../types';

export async function listProjects(): Promise<Project[]> {
  return apiJson<Project[]>('/projects');
}

export async function createProject(name: string): Promise<Project> {
  return apiJson<Project>('/projects', {
    method: 'POST',
    body: JSON.stringify({ name }),
  });
}

export async function deleteProject(id: string): Promise<void> {
  await apiJson<void>(`/projects/${id}`, { method: 'DELETE' });
}
