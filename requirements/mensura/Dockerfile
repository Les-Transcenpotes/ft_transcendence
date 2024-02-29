FROM        debian:bookworm

RUN         apt update -y && \
            apt upgrade -y && \
            apt install -y prometheus

ENTRYPOINT  ["prometheus", "--config.file=/etc/prometheus/prometheus.yml"]
