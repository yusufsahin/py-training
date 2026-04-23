import { getToken, setToken as persistToken } from '../lib/tokenStorage';

let onUnauthorized: (() => void) | null = null;

export function setUnauthorizedHandler(handler: (() => void) | null): void {
  onUnauthorized = handler;
}

function baseUrl(): string {
  const raw = import.meta.env.VITE_API_BASE_URL as string | undefined;
  const u = (raw || 'http://localhost:8000').replace(/\/$/, '');
  return u;
}

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

export async function apiJson<T>(path: string, init: RequestInit = {}): Promise<T> {
  const url = `${baseUrl()}${path}`;
  const headers = new Headers(init.headers);
  const method = (init.method || 'GET').toUpperCase();
  if (method !== 'GET' && method !== 'HEAD' && !headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }
  const token = getToken();
  if (token) headers.set('Authorization', `Bearer ${token}`);

  const res = await fetch(url, { ...init, headers });

  if (res.status === 401) {
    persistToken(null);
    onUnauthorized?.();
  }

  if (res.status === 204) {
    return undefined as T;
  }

  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = (await res.json()) as { detail?: string | unknown };
      if (typeof body.detail === 'string') detail = body.detail;
      else if (Array.isArray(body.detail)) detail = JSON.stringify(body.detail);
    } catch {
      /* ignore */
    }
    throw new ApiError(res.status, detail);
  }

  return (await res.json()) as T;
}
