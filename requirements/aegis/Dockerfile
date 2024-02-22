#---- base image ------------------------------------------------------#

FROM    nginx:1-alpine3.18

#---- ModSecurity -----------------------------------------------------#

RUN     apk update && \
        apk upgrade && \
        apk add wget \
                git \
                libtool \
                autoconf \
                automake \
                build-base \
                yajl-dev \
                geoip-dev \
                libmaxminddb-dev \
                lmdb-dev \
                lua-dev \
                curl-dev \
                libxml2-dev \
                pcre-dev \
                linux-headers

RUN     git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
        cd ModSecurity && \
        git submodule init && \
        git submodule update

RUN     cd ModSecurity && \
        ./build.sh && \
        ./configure && \
        make && \
        make install

#---- ModSecurity connector -------------------------------------------#

RUN     git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
        export NGINX_VERSION=$(nginx -v 2>&1 | cut -d'/' -f2)

RUN     wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
        tar -zxvf nginx-$NGINX_VERSION.tar.gz && \
        cd nginx-$NGINX_VERSION && \
        ./configure --with-compat --add-dynamic-module=../ModSecurity-nginx && \
        make modules && \
        cp objs/ngx_http_modsecurity_module.so /etc/nginx/modules/

#---- config ----------------------------------------------------------#

COPY    conf/nginx.conf /etc/nginx/conf.d/default.conf
COPY    conf/load_module.conf /etc/nginx/nginx.conf
RUN     ln -s /etc/nginx/conf.d/sites-available/nginx.conf /etc/nginx/conf.d/sites-enabled

#---- TSL/SSL certification -------------------------------------------#

RUN     mkdir -p /etc/nginx/ssl && \
        apk add --update --no-cache openssl &&                         \
        openssl req -x509 -nodes                                       \
            -out /etc/nginx/ssl/ft_transcendence.crt                   \
            -keyout /etc/nginx/ssl/ft_transcendence.key                \
            -subj "/C=FR/L=Lyon/CN=batch.42.fr" || \
            { echo "SSL certification failed"; exit 1; }
