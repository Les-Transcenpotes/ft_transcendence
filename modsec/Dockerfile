FROM    alpine:3.18

COPY    requirements.txt /requirements.txt

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
        make