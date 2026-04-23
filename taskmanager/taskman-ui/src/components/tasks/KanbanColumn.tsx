import { useDroppable } from '@dnd-kit/core';
import { SortableContext, verticalListSortingStrategy } from '@dnd-kit/sortable';
import { Task, TaskStatus } from '../../types';
import { SortableTaskCard } from './SortableTaskCard';

interface KanbanColumnProps {
  status: TaskStatus;
  label: string;
  color: string;
  tasks: Task[];
  onTaskClick: (taskId: string) => void;
}

export function KanbanColumn({ status, label, color, tasks, onTaskClick }: KanbanColumnProps) {
  const { setNodeRef } = useDroppable({
    id: status,
  });

  return (
    <div className="flex min-w-[300px] flex-1 flex-col">
      <div className={`mb-3 flex items-center gap-2 rounded-lg ${color} px-3 py-2`}>
        <h2 className="font-semibold">{label}</h2>
        <span className="rounded-full bg-white px-2 py-0.5 text-xs">{tasks.length}</span>
      </div>

      <SortableContext items={tasks.map((t) => t.id)} strategy={verticalListSortingStrategy}>
        <div ref={setNodeRef} className="flex min-h-[200px] flex-1 flex-col gap-3">
          {tasks.map((task) => (
            <SortableTaskCard
              key={task.id}
              task={task}
              onClick={() => onTaskClick(task.id)}
            />
          ))}
        </div>
      </SortableContext>
    </div>
  );
}
