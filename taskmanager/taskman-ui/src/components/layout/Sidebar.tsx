import { useEffect, useState } from 'react';
import { Plus, FolderKanban } from 'lucide-react';

import { useCreateProjectMutation, useProjectsQuery } from '../../hooks/useProjects';
import { useProjectStore } from '../../store/projectStore';
import { Button } from '../ui/button';
import { Input } from '../ui/input';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '../ui/dialog';
import { cn } from '../../lib/utils';

export function Sidebar() {
  const { data: projects = [], isLoading } = useProjectsQuery();
  const createProject = useCreateProjectMutation();
  const selectedProjectId = useProjectStore((s) => s.selectedProjectId);
  const selectProject = useProjectStore((s) => s.selectProject);

  const [newProjectName, setNewProjectName] = useState('');
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (isLoading) return;
    if (!projects.length) {
      selectProject(null);
      return;
    }
    const valid = selectedProjectId && projects.some((p) => p.id === selectedProjectId);
    if (!valid) {
      selectProject(projects[0].id);
    }
  }, [isLoading, projects, selectedProjectId, selectProject]);

  const handleAddProject = async () => {
    const name = newProjectName.trim();
    if (!name) return;
    try {
      const created = await createProject.mutateAsync(name);
      setNewProjectName('');
      setIsOpen(false);
      selectProject(created.id);
    } catch {
      /* toast optional */
    }
  };

  return (
    <aside className="w-64 border-r bg-muted/30">
      <div className="flex h-full flex-col">
        <div className="p-4">
          <Dialog open={isOpen} onOpenChange={setIsOpen}>
            <DialogTrigger asChild>
              <Button className="w-full">
                <Plus className="h-4 w-4" />
                Yeni Proje
              </Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Yeni Proje Oluştur</DialogTitle>
                <DialogDescription>
                  Projenize bir isim verin ve görevlerinizi organize edin.
                </DialogDescription>
              </DialogHeader>
              <div className="grid gap-4 py-4">
                <Input
                  placeholder="Proje adı"
                  value={newProjectName}
                  onChange={(e) => setNewProjectName(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter') void handleAddProject();
                  }}
                />
              </div>
              <DialogFooter>
                <Button variant="outline" onClick={() => setIsOpen(false)}>
                  İptal
                </Button>
                <Button onClick={() => void handleAddProject()} disabled={createProject.isPending}>
                  Oluştur
                </Button>
              </DialogFooter>
            </DialogContent>
          </Dialog>
        </div>

        <div className="flex-1 overflow-y-auto px-2">
          {isLoading ? (
            <div className="px-3 py-2 text-sm text-muted-foreground">Projeler yükleniyor…</div>
          ) : (
            <div className="space-y-1">
              {projects.map((project) => (
                <button
                  key={project.id}
                  type="button"
                  onClick={() => selectProject(project.id)}
                  className={cn(
                    'flex w-full items-center gap-2 rounded-lg px-3 py-2 text-left transition-colors hover:bg-accent',
                    selectedProjectId === project.id && 'bg-accent'
                  )}
                >
                  <FolderKanban className="h-4 w-4 shrink-0" />
                  <span className="truncate">{project.name}</span>
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </aside>
  );
}
