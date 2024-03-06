FROM    debian:bookworm

RUN     apt update -y && \
        apt upgrade -y && \
        apt install wget -y && \
        wget https://github.com/sysulq/nginx-vts-exporter/releases/download/v0.10.8/nginx-vtx-exporter_0.10.8_linux_amd64.tar.gz && \
        tar -xvf nginx-vtx-exporter_0.10.8_linux_amd64.tar.gz && \
        rm nginx-vtx-exporter_0.10.8_linux_amd64.tar.gz

ENTRYPOINT ["./nginx-vtx-exporter", "-nginx.scrape_uri", "https://aegis/status/format/json"]