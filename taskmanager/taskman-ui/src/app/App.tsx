import { Navbar } from '../components/layout/Navbar';
import { Sidebar } from '../components/layout/Sidebar';
import { TaskFilters } from '../components/tasks/TaskFilters';
import { KanbanBoard } from '../components/tasks/KanbanBoard';
import { TaskList } from '../components/tasks/TaskList';
import { useProjectsQuery } from '../hooks/useProjects';
import { useTaskStore } from '../store/taskStore';
import { useProjectStore } from '../store/projectStore';

export default function App() {
  const viewMode = useTaskStore((state) => state.viewMode);
  const { data: projects = [] } = useProjectsQuery();
  const selectedProjectId = useProjectStore((state) => state.selectedProjectId);
  const selectedProject = projects.find((p) => p.id === selectedProjectId);

  return (
    <div className="flex h-screen flex-col bg-background">
      <Navbar />

      <div className="flex flex-1 overflow-hidden">
        <Sidebar />

        <main className="flex flex-1 flex-col overflow-hidden">
          {selectedProject ? (
            <>
              <TaskFilters />
              <div className="flex-1 overflow-auto">
                {viewMode === 'kanban' ? <KanbanBoard /> : <TaskList />}
              </div>
            </>
          ) : (
            <div className="flex h-full items-center justify-center text-muted-foreground">
              Başlamak için bir proje seçin veya yeni bir proje oluşturun
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
