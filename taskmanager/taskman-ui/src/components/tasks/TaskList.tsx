import { useMemo, useState } from 'react';

import { useTasksQuery } from '../../hooks/useTasks';
import { useProjectStore } from '../../store/projectStore';
import { useTaskStore } from '../../store/taskStore';
import { TaskCard } from './TaskCard';
import { TaskModal } from './TaskModal';

export function TaskList() {
  const { filterStatus, filterPriority } = useTaskStore();
  const selectedProjectId = useProjectStore((s) => s.selectedProjectId);
  const { data: tasks = [] } = useTasksQuery(selectedProjectId);
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);

  const filteredTasks = useMemo(() => {
    return tasks.filter((task) => {
      if (task.is_deleted) return false;
      if (filterStatus !== 'all' && task.status !== filterStatus) return false;
      if (filterPriority !== 'all' && task.priority !== filterPriority) return false;
      return true;
    });
  }, [tasks, filterStatus, filterPriority]);

  return (
    <>
      <div className="space-y-3 p-6">
        {filteredTasks.length === 0 ? (
          <div className="flex h-64 items-center justify-center text-muted-foreground">
            Henüz görev bulunmuyor. Yeni görev ekleyerek başlayın!
          </div>
        ) : (
          filteredTasks.map((task) => (
            <TaskCard key={task.id} task={task} onClick={() => setEditingTaskId(task.id)} />
          ))
        )}
      </div>

      {editingTaskId && (
        <TaskModal taskId={editingTaskId} onClose={() => setEditingTaskId(null)} />
      )}
    </>
  );
}
