import { create } from 'zustand';

import { fetchMe, loginRequest, registerRequest } from '../api/auth';
import { setUnauthorizedHandler } from '../api/client';
import { getToken, setToken } from '../lib/tokenStorage';
import { queryClient } from '../queryClient';
import type { Profile } from '../types';

interface AuthState {
  user: Profile | null;
  token: string | null;
  initialized: boolean;
  bootstrap: () => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, fullName: string) => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: null,
  initialized: false,

  bootstrap: async () => {
    const token = getToken();
    set({ initialized: false, token });
    if (!token) {
      set({ user: null, token: null, initialized: true });
      return;
    }
    try {
      const user = await fetchMe();
      set({ user, token, initialized: true });
    } catch {
      setToken(null);
      set({ user: null, token: null, initialized: true });
    }
  },

  login: async (email: string, password: string) => {
    const { access_token } = await loginRequest(email, password);
    setToken(access_token);
    set({ token: access_token });
    const user = await fetchMe();
    set({ user });
  },

  register: async (email: string, password: string, fullName: string) => {
    const { access_token } = await registerRequest(email, password, fullName);
    setToken(access_token);
    set({ token: access_token });
    const user = await fetchMe();
    set({ user });
  },

  logout: () => {
    setToken(null);
    queryClient.clear();
    set({ user: null, token: null });
  },
}));

setUnauthorizedHandler(() => {
  setToken(null);
  queryClient.clear();
  useAuthStore.setState({ user: null, token: null, initialized: true });
});
