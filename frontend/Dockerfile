FROM node:alpine

WORKDIR /app/webapp
COPY ./package*.json ./

# Install dependencies
RUN npm install --production

# Copy all files
COPY ./ ./

# Build app
RUN npm run build

USER node

EXPOSE 3000

CMD [ "npm", "start" ]