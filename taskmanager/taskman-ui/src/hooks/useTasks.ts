import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import * as tasksApi from '../api/tasks';

export function useTasksQuery(projectId: string | null) {
  return useQuery({
    queryKey: ['tasks', projectId],
    queryFn: () => tasksApi.listTasks(projectId as string),
    enabled: Boolean(projectId),
  });
}

export function useCreateTaskMutation() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (payload: tasksApi.TaskCreatePayload) => tasksApi.createTask(payload),
    onSuccess: (_data, variables) => {
      qc.invalidateQueries({ queryKey: ['tasks', variables.project_id] });
    },
  });
}

export function usePatchTaskMutation(projectId: string | null) {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: ({ id, payload }: { id: string; payload: tasksApi.TaskUpdatePayload }) =>
      tasksApi.patchTask(id, payload),
    onSuccess: () => {
      if (projectId) qc.invalidateQueries({ queryKey: ['tasks', projectId] });
    },
  });
}
