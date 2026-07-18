# Stage 1: Build
FROM node:18-alpine AS build
WORKDIR /app
# Копируем файлы зависимостей
COPY package.json package-lock.json ./
# Устанавливаем зависимости
RUN npm ci
# Копируем исходный код
COPY . .
# Собираем приложение
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
# Копируем конфигурацию nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Копируем собранные файлы из build stage
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
