import { apiJson } from './client';
import type { Profile } from '../types';

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export async function loginRequest(email: string, password: string): Promise<TokenResponse> {
  return apiJson<TokenResponse>('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
}

export async function registerRequest(
  email: string,
  password: string,
  full_name: string
): Promise<TokenResponse> {
  return apiJson<TokenResponse>('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ email, password, full_name }),
  });
}

export async function fetchMe(): Promise<Profile> {
  return apiJson<Profile>('/auth/me');
}
