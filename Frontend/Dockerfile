FROM node:20.11 as angular

WORKDIR /app

COPY . /app

RUN npm install -g @angular/cli
RUN npm install
RUN npm run build

CMD ng serve --host 0.0.0.0 --port 4200