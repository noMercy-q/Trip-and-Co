import axios from 'axios';
import store from '@/store';

export const backendBaseURL = "http://localhost:8000"

const apiClient = axios.create({
  baseURL: backendBaseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(config => {
  const token = store.state.auth.token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  console.log('token: ', token)
  return config;
});

export default apiClient;