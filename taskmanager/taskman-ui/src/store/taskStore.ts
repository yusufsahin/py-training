import { create } from 'zustand';

import type { TaskPriority, TaskStatus } from '../types';

interface TaskUiState {
  viewMode: 'kanban' | 'list';
  filterStatus: TaskStatus | 'all';
  filterPriority: TaskPriority | 'all';
  setViewMode: (mode: 'kanban' | 'list') => void;
  setFilterStatus: (status: TaskStatus | 'all') => void;
  setFilterPriority: (priority: TaskPriority | 'all') => void;
}

export const useTaskStore = create<TaskUiState>((set) => ({
  viewMode: 'kanban',
  filterStatus: 'all',
  filterPriority: 'all',
  setViewMode: (mode) => set({ viewMode: mode }),
  setFilterStatus: (status) => set({ filterStatus: status }),
  setFilterPriority: (priority) => set({ filterPriority: priority }),
}));
