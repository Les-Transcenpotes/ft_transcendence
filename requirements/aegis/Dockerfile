#---- base image ------------------------------------------------------#

FROM    nginx:1-alpine3.18

#---- config ----------------------------------------------------------#

COPY    conf/nginx.conf /etc/nginx/conf.d/default.conf

#---- TSL/SSL certification -------------------------------------------#

RUN     mkdir -p /etc/nginx/ssl && \
        apk add --update --no-cache openssl &&                         \
        openssl req -x509 -nodes                                       \
            -out /etc/nginx/ssl/ft_transcendence.crt                   \
            -keyout /etc/nginx/ssl/ft_transcendence.key                \
            -subj "/C=FR/L=Lyon/CN=batch.42.fr"
