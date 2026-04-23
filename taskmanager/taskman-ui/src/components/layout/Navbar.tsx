import { LogOut, User } from 'lucide-react';
import { useAuthStore } from '../../store/authStore';
import { Button } from '../ui/button';

export function Navbar() {
  const { user, logout } = useAuthStore();

  return (
    <nav className="border-b bg-background">
      <div className="flex h-16 items-center px-6">
        <div className="flex items-center gap-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
            <span className="font-bold">T</span>
          </div>
          <span className="font-semibold">TaskFlow</span>
        </div>

        <div className="ml-auto flex items-center gap-4">
          {user && (
            <>
              <div className="flex items-center gap-2">
                <User className="h-4 w-4 text-muted-foreground" />
                <span className="text-sm">{user.full_name}</span>
              </div>
              <Button variant="ghost" size="sm" onClick={logout}>
                <LogOut className="h-4 w-4" />
                Çıkış
              </Button>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
