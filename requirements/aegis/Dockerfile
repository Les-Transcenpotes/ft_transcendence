#---- base image ------------------------------------------------------#

FROM    nginx:1-alpine3.18

#---- ModSecurity -----------------------------------------------------#

COPY    requirements.txt ./requirements.txt

RUN     apk update && \
        apk upgrade && \
        cat requirements.txt | xargs apk add --no-cache && \
        rm requirements.txt && \
        git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
        cd ModSecurity && \
        git submodule init && \
        git submodule update && \
        ./build.sh && \
        ./configure && \
        make && \
        make install

#---- ModSecurity connector -------------------------------------------#

RUN     git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
        export NGINX_VERSION=$(nginx -v 2>&1 | cut -d'/' -f2) && \
        wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
        tar -zxvf nginx-$NGINX_VERSION.tar.gz && \
        rm nginx-$NGINX_VERSION.tar.gz && \
        curl -fSL https://github.com/vozlt/nginx-module-vts/archive/refs/tags/v0.2.2.tar.gz | tar xzf - -C /tmp && \
        cd nginx-$NGINX_VERSION && \
        ./configure --with-compat --add-dynamic-module=../ModSecurity-nginx --add-dynamic-module=/tmp/nginx-module-vts-0.2.2 && \
        make && \
        make install && \
        cp objs/ngx_http_vhost_traffic_status_module.so /etc/nginx/modules/ && \
        cp objs/ngx_http_modsecurity_module.so /etc/nginx/modules/ && \
        mkdir /etc/nginx/modsec/ && \
        cp /ModSecurity/unicode.mapping /etc/nginx/modsec/
#        cd /etc/nginx/modsec/ && \
#        wget https://github.com/coreruleset/coreruleset/archive/refs/tags/v4.0.0.tar.gz && \
#        tar -xvf v4.0.0.tar.gz && \
#        rm v4.0.0.tar.gz && \
#        cp coreruleset-4.0.0/crs-setup.conf.example coreruleset-4.0.0/crs-setup.conf


COPY    conf/modsec-config.conf /etc/nginx/modsec/modsec-config.conf
COPY    conf/modsecurity.conf /etc/nginx/modsec/modsecurity.conf
COPY    conf/no-http-fingerprint.conf /etc/nginx/modsec/no-http-fingerprint.conf
COPY    conf/aegis-whitelist.conf /etc/nginx/modsec/aegis-whitelist.conf
#COPY    conf/crs-setup.conf /etc/nginx/modsec/coreruleset-4.0.0/crs-setup.conf
#COPY    conf/grafana_whitelist.conf /etc/nginx/modsec/grafana_whitelist.conf
#COPY    conf/prometheus_whitelist.conf /etc/nginx/modsec/prometheus_whitelist.conf
COPY    conf/proxy.conf /etc/nginx/nginx.conf

#---- config ----------------------------------------------------------#

RUN     ln -s /etc/nginx/conf.d/sites-available/nginx.conf /etc/nginx/conf.d/sites-enabled

#---- TSL/SSL certification -------------------------------------------#

RUN     mkdir -p /data/nginx/cache &&                                  \
        mkdir -p /etc/nginx/ssl &&                                     \
        apk add --update --no-cache openssl &&                         \
        openssl req -x509 -nodes                                       \
            -out /etc/nginx/ssl/ft_transcendence.crt                   \
            -keyout /etc/nginx/ssl/ft_transcendence.key                \
            -subj "/C=FR/L=Lyon/CN=batch42.me" || \
            { echo "SSL certification failed"; exit 1; }
