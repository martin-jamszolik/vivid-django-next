FROM nginx:stable-alpine

# Remove any existing config files
RUN rm /etc/nginx/conf.d/*

COPY ./nginx.conf /etc/nginx/conf.d/

# Expose the listening port
EXPOSE 80

# Launch NGINX
CMD [ "nginx", "-g", "daemon off;" ]
