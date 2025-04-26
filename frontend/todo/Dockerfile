# Frontend Dockerfile
FROM node:20-alpine as build

WORKDIR /app

# Copy package.json and install dependencies
COPY todo/package.json .
COPY todo/package-lock.json .
RUN npm install

# Copy all frontend source code
COPY todo/ .

# Build the React app
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=${REACT_APP_API_URL}
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]