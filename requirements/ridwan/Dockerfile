FROM debian:bookworm

RUN apt update -y
RUN apt upgrade -y

RUN apt install -y nginx

RUN apt-get install -y \
    bison \
    build-essential \
    ca-certificates \
    curl \
    dh-autoreconf \
    doxygen \
    flex \
    gawk \
    git \
    iputils-ping \
    libcurl4-gnutls-dev \
    libexpat1-dev \
    libgeoip-dev \
    liblmdb-dev \
    libpcre3-dev \
    libssl-dev \
    libtool \
    libxml2 \
    libxml2-dev \
    libyajl-dev \
    locales \
    lua5.3-dev \
    pkg-config \
    wget \
    zlib1g-dev \
    libxslt1-dev \
    libgd-dev

RUN apt install -y git
RUN apt install -y clang

RUN cd /opt/ && git clone https://github.com/SpiderLabs/ModSecurity
RUN cd /opt/ModSecurity && git submodule init && git submodule update
RUN cd /opt/ModSecurity/ && ./build.sh
RUN cd /opt/ModSecurity/ && ./configure && make && make install

RUN cd /opt && git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git

RUN cd /opt && wget http://nginx.org/download/nginx-1.22.1.tar.gz && tar -xvzmf nginx-1.22.1.tar.gz && rm nginx-1.22.1.tar.gz

COPY entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]