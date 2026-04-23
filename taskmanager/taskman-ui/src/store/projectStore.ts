import { create } from 'zustand';

interface ProjectUiState {
  selectedProjectId: string | null;
  selectProject: (id: string | null) => void;
}

export const useProjectStore = create<ProjectUiState>((set) => ({
  selectedProjectId: null,
  selectProject: (id) => set({ selectedProjectId: id }),
}));
