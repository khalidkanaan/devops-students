FROM nginx:alpine

WORKDIR /home/app

#add our config to the container
COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

#I don't think custom cmd is needed
CMD ["nginx","-g","daemon off;"]