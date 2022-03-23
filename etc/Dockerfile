# The image to pull the base configuration from
FROM nginx:mainline-alpine

EXPOSE 81

# Copy the custom default.conf from the WORKDIR (.) and overwrite the existing internal configuration in the NGINX container
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf