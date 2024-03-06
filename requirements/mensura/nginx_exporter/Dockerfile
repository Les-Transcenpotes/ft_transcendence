FROM    debian:bookworm

RUN     apt update -y && \
        apt upgrade -y && \
        apt install wget \
                    libc6 \
                    daemon -y && \
        wget http://ftp.br.debian.org/debian/pool/main/p/prometheus-nginx-exporter/prometheus-nginx-exporter_1.1.0-1_amd64.deb && \
        dpkg -i prometheus-nginx-exporter_1.1.0-1_amd64.deb

ENTRYPOINT ["prometheus-nginx-exporter"]