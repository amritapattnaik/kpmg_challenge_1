FROM node:14-alpine3.15 as build

RUN mkdir /app
# Create app directory
WORKDIR /app
COPY . .

RUN npm install && npm run build

FROM nginx:1.17.1-alpine

RUN rm -rf /usr/share/nginx/html/* && rm -rf /etc/nginx/nginx.conf

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/dist/my-app /usr/share/nginx/html

EXPOSE 3000
