import { Filter, LayoutGrid, List, Plus } from 'lucide-react';
import { useTaskStore } from '../../store/taskStore';
import { Button } from '../ui/button';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '../ui/select';
import { TaskPriority, TaskStatus } from '../../types';
import { useState } from 'react';
import { TaskModal } from './TaskModal';

export function TaskFilters() {
  const {
    viewMode,
    setViewMode,
    filterStatus,
    setFilterStatus,
    filterPriority,
    setFilterPriority,
  } = useTaskStore();
  const [showAddTask, setShowAddTask] = useState(false);

  return (
    <>
      <div className="flex items-center justify-between border-b bg-background p-4">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2">
            <Filter className="h-4 w-4 text-muted-foreground" />
            <Select
              value={filterStatus}
              onValueChange={(v) => setFilterStatus(v as TaskStatus | 'all')}
            >
              <SelectTrigger className="w-[140px]">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">Tüm Durumlar</SelectItem>
                <SelectItem value="todo">Yapılacak</SelectItem>
                <SelectItem value="in_progress">Devam Ediyor</SelectItem>
                <SelectItem value="done">Tamamlandı</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <Select
            value={filterPriority}
            onValueChange={(v) => setFilterPriority(v as TaskPriority | 'all')}
          >
            <SelectTrigger className="w-[140px]">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">Tüm Öncelikler</SelectItem>
              <SelectItem value="low">Düşük</SelectItem>
              <SelectItem value="medium">Orta</SelectItem>
              <SelectItem value="high">Yüksek</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="flex items-center gap-2">
          <div className="flex rounded-lg border">
            <Button
              variant={viewMode === 'kanban' ? 'secondary' : 'ghost'}
              size="sm"
              onClick={() => setViewMode('kanban')}
              className="rounded-r-none"
            >
              <LayoutGrid className="h-4 w-4" />
              Kanban
            </Button>
            <Button
              variant={viewMode === 'list' ? 'secondary' : 'ghost'}
              size="sm"
              onClick={() => setViewMode('list')}
              className="rounded-l-none"
            >
              <List className="h-4 w-4" />
              Liste
            </Button>
          </div>

          <Button onClick={() => setShowAddTask(true)}>
            <Plus className="h-4 w-4" />
            Yeni Görev
          </Button>
        </div>
      </div>

      {showAddTask && <TaskModal onClose={() => setShowAddTask(false)} />}
    </>
  );
}
