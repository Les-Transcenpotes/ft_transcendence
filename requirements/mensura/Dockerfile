FROM        debian:bookworm

RUN         apt update -y && \
            apt upgrade -y && \
            apt install -y prometheus

#COPY conf/prometheus.yml /etc/prometheus/prometheus.yml

ENTRYPOINT  ["prometheus", "--config.file=/etc/prometheus/prometheus.yml", "--web.listen-address=0.0.0.0:8011", "--web.external-url=https://localhost:8011/mensura/"]
