#! /bin/ash

export NGINX_VERSION=$(nginx -v 2>&1 | cut -d'/' -f2)
wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
tar zxvf nginx-$NGINX_VERSION.tar.gz