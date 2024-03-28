FROM        debian:bookworm

ENV VAULT_ADDR=http://0.0.0.0:8200/

COPY        conf/config.hcl /config.hcl

RUN         apt update -y && \
            apt upgrade -y && \
            apt install -y gpg wget lsb-release curl && \
            wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
            gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint && \
            echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list && \
            apt update -y && \
            apt install -y vault

COPY        ./tools/script.sh /script.sh

RUN         chmod +x /script.sh

CMD         vault server -config=config.hcl & \
            sleep 1 && \
            ./script.sh && \
            tail -f /dev/null