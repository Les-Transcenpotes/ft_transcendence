#---- base image ------------------------------------------------------#

FROM    nginx:1-alpine3.18

#---- config ----------------------------------------------------------#

COPY    conf/nginx.conf /etc/nginx/conf.d/sites-available/nginx.conf
RUN     ln -s /etc/nginx/conf.d/sites-available/nginx.conf /etc/nginx/conf.d/sites-enabled

#---- TSL/SSL certification -------------------------------------------#

RUN     mkdir -p /etc/nginx/ssl && \
        apk add --update --no-cache openssl &&                         \
        openssl req -x509 -nodes                                       \
            -out /etc/nginx/ssl/ft_transcendence.crt                   \
            -keyout /etc/nginx/ssl/ft_transcendence.key                \
            -subj "/C=FR/L=Lyon/CN=batch.42.fr" || \
            { echo "SSL certification failed"; exit 1; }
