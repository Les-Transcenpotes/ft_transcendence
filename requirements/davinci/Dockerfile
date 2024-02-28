FROM        debian:bookworm

RUN         apt update -y && \
            apt upgrade -y && \
            apt install -y  apt-transport-https \
                            software-properties-common \
                            vim \
                            curl \
                            wget && \
            mkdir -p /etc/apt/keyrings/ && \
            wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | tee /etc/apt/keyrings/grafana.gpg > /dev/null && \
            echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | tee -a /etc/apt/sources.list.d/grafana.list && \
            apt update -y && \
            apt install grafana-enterprise -y

COPY        conf/grafana.ini /etc/grafana/grafana.ini

ENTRYPOINT ["grafana-server", "--config=/etc/grafana/grafana.ini", "--homepath=/usr/share/grafana/"]