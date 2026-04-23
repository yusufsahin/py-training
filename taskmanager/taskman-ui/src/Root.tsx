import { useEffect } from 'react';

import App from './app/App';
import { AuthScreen } from './components/auth/AuthScreen';
import { useAuthStore } from './store/authStore';

export function Root() {
  const bootstrap = useAuthStore((s) => s.bootstrap);
  const initialized = useAuthStore((s) => s.initialized);
  const user = useAuthStore((s) => s.user);

  useEffect(() => {
    void bootstrap();
  }, [bootstrap]);

  if (!initialized) {
    return (
      <div className="flex h-screen items-center justify-center text-muted-foreground">
        Yükleniyor…
      </div>
    );
  }

  if (!user) {
    return <AuthScreen />;
  }

  return <App />;
}
