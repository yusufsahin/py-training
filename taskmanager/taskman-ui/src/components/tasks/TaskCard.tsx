import { useState } from 'react';
import { Calendar, Flag, MoreVertical, Trash2 } from 'lucide-react';
import { format } from 'date-fns';
import { tr } from 'date-fns/locale';

import { usePatchTaskMutation } from '../../hooks/useTasks';
import { useProjectStore } from '../../store/projectStore';
import type { Task, TaskPriority } from '../../types';
import { Badge } from '../ui/badge';
import { Button } from '../ui/button';
import { Card } from '../ui/card';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '../ui/dialog';

interface TaskCardProps {
  task: Task;
  onClick?: () => void;
}

const priorityConfig: Record<TaskPriority, { label: string; color: string }> = {
  low: { label: 'Düşük', color: 'text-green-600' },
  medium: { label: 'Orta', color: 'text-yellow-600' },
  high: { label: 'Yüksek', color: 'text-red-600' },
};

export function TaskCard({ task, onClick }: TaskCardProps) {
  const selectedProjectId = useProjectStore((s) => s.selectedProjectId);
  const patchTask = usePatchTaskMutation(selectedProjectId);
  const [showDeleteDialog, setShowDeleteDialog] = useState(false);

  const handleDelete = async () => {
    try {
      await patchTask.mutateAsync({ id: task.id, payload: { is_deleted: true } });
      setShowDeleteDialog(false);
    } catch {
      /* ignore */
    }
  };

  return (
    <>
      <Card
        className="group cursor-pointer transition-shadow hover:shadow-md"
        onClick={onClick}
      >
        <div className="p-4">
          <div className="mb-2 flex items-start justify-between gap-2">
            <h3 className="line-clamp-2 flex-1 font-medium">{task.title}</h3>
            <Button
              variant="ghost"
              size="icon"
              className="h-6 w-6 opacity-0 transition-opacity group-hover:opacity-100"
              onClick={(e) => {
                e.stopPropagation();
                setShowDeleteDialog(true);
              }}
            >
              <MoreVertical className="h-4 w-4" />
            </Button>
          </div>

          {task.description && (
            <p className="mb-3 line-clamp-2 text-sm text-muted-foreground">
              {task.description}
            </p>
          )}

          <div className="flex flex-wrap items-center gap-2">
            <div className={`flex items-center gap-1 text-xs ${priorityConfig[task.priority].color}`}>
              <Flag className="h-3 w-3" />
              {priorityConfig[task.priority].label}
            </div>

            {task.due_date && (
              <div className="flex items-center gap-1 text-xs text-muted-foreground">
                <Calendar className="h-3 w-3" />
                {format(new Date(task.due_date), 'd MMM', { locale: tr })}
              </div>
            )}
          </div>

          {task.labels.length > 0 && (
            <div className="mt-2 flex flex-wrap gap-1">
              {task.labels.map((label) => (
                <Badge
                  key={label.id}
                  variant="outline"
                  style={{ borderColor: label.color, color: label.color }}
                  className="text-xs"
                >
                  {label.name}
                </Badge>
              ))}
            </div>
          )}
        </div>
      </Card>

      <Dialog open={showDeleteDialog} onOpenChange={setShowDeleteDialog}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Görevi Sil</DialogTitle>
            <DialogDescription>
              Bu görevi silmek istediğinizden emin misiniz? Bu işlem geri alınamaz.
            </DialogDescription>
          </DialogHeader>
          <DialogFooter>
            <Button variant="outline" onClick={() => setShowDeleteDialog(false)}>
              İptal
            </Button>
            <Button variant="destructive" onClick={() => void handleDelete()} disabled={patchTask.isPending}>
              <Trash2 className="h-4 w-4" />
              Sil
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </>
  );
}
