#!/bin/sh

docker run -d -e NGINX_ENTRYPOINT_QUIET_LOGS=1 nginx
