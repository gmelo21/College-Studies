import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/STH': {
        target: 'http://191.235.32.167:8666',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/STH/, '/STH')
      }
    }
  }
});
