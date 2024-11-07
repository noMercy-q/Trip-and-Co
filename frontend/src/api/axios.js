import axios from 'axios';
import store from '@/store'; // подключите Vuex, если храните там токен

const apiClient = axios.create({
  baseURL: 'https://your-backend-url.com',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Добавьте интерсептор для автоматического добавления токена
apiClient.interceptors.request.use(config => {
  const token = store.state.auth.token; // предположим, токен хранится в auth модуля
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default apiClient;