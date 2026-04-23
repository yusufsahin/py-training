import { useEffect, useState } from 'react';

import { useCreateTaskMutation, usePatchTaskMutation, useTasksQuery } from '../../hooks/useTasks';
import { useProjectStore } from '../../store/projectStore';
import type { Task, TaskPriority, TaskStatus } from '../../types';
import { Button } from '../ui/button';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '../ui/dialog';
import { Input } from '../ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '../ui/select';
import { Textarea } from '../ui/textarea';

interface TaskModalProps {
  taskId?: string | null;
  onClose: () => void;
}

export function TaskModal({ taskId, onClose }: TaskModalProps) {
  const selectedProjectId = useProjectStore((s) => s.selectedProjectId);
  const { data: tasks = [] } = useTasksQuery(selectedProjectId);
  const createTask = useCreateTaskMutation();
  const patchTask = usePatchTaskMutation(selectedProjectId);

  const existingTask: Task | undefined = taskId ? tasks.find((t) => t.id === taskId) : undefined;

  const [title, setTitle] = useState(existingTask?.title || '');
  const [description, setDescription] = useState(existingTask?.description || '');
  const [status, setStatus] = useState<TaskStatus>(existingTask?.status || 'todo');
  const [priority, setPriority] = useState<TaskPriority>(existingTask?.priority || 'medium');
  const [dueDate, setDueDate] = useState(
    existingTask?.due_date ? new Date(existingTask.due_date).toISOString().split('T')[0] : ''
  );

  useEffect(() => {
    setTitle(existingTask?.title || '');
    setDescription(existingTask?.description || '');
    setStatus(existingTask?.status || 'todo');
    setPriority(existingTask?.priority || 'medium');
    setDueDate(
      existingTask?.due_date ? new Date(existingTask.due_date).toISOString().split('T')[0] : ''
    );
  }, [existingTask]);

  const handleSubmit = async () => {
    if (!title.trim() || !selectedProjectId) return;

    try {
      if (existingTask) {
        await patchTask.mutateAsync({
          id: existingTask.id,
          payload: {
            title,
            description: description || undefined,
            status,
            priority,
            due_date: dueDate ? `${dueDate}T12:00:00.000Z` : null,
            label_ids: existingTask.labels.map((l) => l.id),
          },
        });
      } else {
        await createTask.mutateAsync({
          project_id: selectedProjectId,
          title,
          description: description || undefined,
          status,
          priority,
          due_date: dueDate ? `${dueDate}T12:00:00.000Z` : undefined,
          position: 0,
        });
      }
      onClose();
    } catch {
      /* ignore */
    }
  };

  const busy = createTask.isPending || patchTask.isPending;

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>{existingTask ? 'Görevi Düzenle' : 'Yeni Görev'}</DialogTitle>
          <DialogDescription>
            {existingTask
              ? 'Görev detaylarını güncelleyin'
              : 'Yeni bir görev oluşturun ve takip edin'}
          </DialogDescription>
        </DialogHeader>

        <div className="grid gap-4 py-4">
          <div className="grid gap-2">
            <label className="text-sm font-medium">Başlık</label>
            <Input
              placeholder="Görev başlığı"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </div>

          <div className="grid gap-2">
            <label className="text-sm font-medium">Açıklama</label>
            <Textarea
              placeholder="Görev detayları (opsiyonel)"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows={4}
            />
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div className="grid gap-2">
              <label className="text-sm font-medium">Durum</label>
              <Select value={status} onValueChange={(v) => setStatus(v as TaskStatus)}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="todo">Yapılacak</SelectItem>
                  <SelectItem value="in_progress">Devam Ediyor</SelectItem>
                  <SelectItem value="done">Tamamlandı</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="grid gap-2">
              <label className="text-sm font-medium">Öncelik</label>
              <Select value={priority} onValueChange={(v) => setPriority(v as TaskPriority)}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="low">Düşük</SelectItem>
                  <SelectItem value="medium">Orta</SelectItem>
                  <SelectItem value="high">Yüksek</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="grid gap-2">
              <label className="text-sm font-medium">Son Tarih</label>
              <Input type="date" value={dueDate} onChange={(e) => setDueDate(e.target.value)} />
            </div>
          </div>
        </div>

        <DialogFooter>
          <Button variant="outline" onClick={onClose}>
            İptal
          </Button>
          <Button onClick={() => void handleSubmit()} disabled={busy}>
            {existingTask ? 'Güncelle' : 'Oluştur'}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
