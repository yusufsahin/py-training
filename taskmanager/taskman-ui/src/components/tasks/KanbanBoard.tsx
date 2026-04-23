import { useMemo, useState } from 'react';
import {
  DndContext,
  DragEndEvent,
  DragOverlay,
  DragStartEvent,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import { SortableContext, verticalListSortingStrategy } from '@dnd-kit/sortable';

import { usePatchTaskMutation, useTasksQuery } from '../../hooks/useTasks';
import { useProjectStore } from '../../store/projectStore';
import { useTaskStore } from '../../store/taskStore';
import type { TaskStatus } from '../../types';
import { KanbanColumn } from './KanbanColumn';
import { TaskCard } from './TaskCard';
import { TaskModal } from './TaskModal';

const statusConfig: Record<TaskStatus, { label: string; color: string }> = {
  todo: { label: 'Yapılacak', color: 'bg-slate-200' },
  in_progress: { label: 'Devam Ediyor', color: 'bg-blue-200' },
  done: { label: 'Tamamlandı', color: 'bg-green-200' },
};

export function KanbanBoard() {
  const { filterStatus, filterPriority } = useTaskStore();
  const selectedProjectId = useProjectStore((s) => s.selectedProjectId);
  const { data: tasks = [] } = useTasksQuery(selectedProjectId);
  const patchTask = usePatchTaskMutation(selectedProjectId);

  const [activeTaskId, setActiveTaskId] = useState<string | null>(null);
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 8,
      },
    })
  );

  const filteredTasks = useMemo(() => {
    return tasks.filter((task) => {
      if (task.is_deleted) return false;
      if (filterStatus !== 'all' && task.status !== filterStatus) return false;
      if (filterPriority !== 'all' && task.priority !== filterPriority) return false;
      return true;
    });
  }, [tasks, filterStatus, filterPriority]);

  const tasksByStatus = useMemo(() => {
    const grouped: Record<TaskStatus, typeof filteredTasks> = {
      todo: [],
      in_progress: [],
      done: [],
    };

    filteredTasks.forEach((task) => {
      grouped[task.status].push(task);
    });

    return grouped;
  }, [filteredTasks]);

  const handleDragStart = (event: DragStartEvent) => {
    setActiveTaskId(event.active.id as string);
  };

  const handleDragEnd = async (event: DragEndEvent) => {
    const { active, over } = event;

    if (!over) {
      setActiveTaskId(null);
      return;
    }

    const taskId = active.id as string;
    const newStatus = over.id as TaskStatus;

    if (Object.keys(statusConfig).includes(newStatus)) {
      try {
        await patchTask.mutateAsync({ id: taskId, payload: { status: newStatus } });
      } catch {
        /* ignore */
      }
    }

    setActiveTaskId(null);
  };

  const activeTask = activeTaskId ? tasks.find((t) => t.id === activeTaskId) : null;

  return (
    <>
      <DndContext sensors={sensors} onDragStart={handleDragStart} onDragEnd={handleDragEnd}>
        <div className="flex h-full gap-4 overflow-x-auto p-6">
          {(Object.keys(statusConfig) as TaskStatus[]).map((status) => (
            <KanbanColumn
              key={status}
              status={status}
              label={statusConfig[status].label}
              color={statusConfig[status].color}
              tasks={tasksByStatus[status]}
              onTaskClick={(taskId) => setEditingTaskId(taskId)}
            />
          ))}
        </div>

        <DragOverlay>
          {activeTask && (
            <div className="rotate-3 opacity-80">
              <TaskCard task={activeTask} />
            </div>
          )}
        </DragOverlay>
      </DndContext>

      {editingTaskId && (
        <TaskModal taskId={editingTaskId} onClose={() => setEditingTaskId(null)} />
      )}
    </>
  );
}
