FROM debian:bookworm

RUN apt update -y
RUN apt upgrade -y
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

RUN cd /opt/ && git clone https://github.com/SpiderLabs/ModSecurity
RUN cd /opt/ModSecurity && git submodule init && git submodule update


#ADD prometheus.yml /etc/prometheus/