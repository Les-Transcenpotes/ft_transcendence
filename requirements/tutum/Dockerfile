FROM        debian:bookworm

COPY        ./tools/entrypoint.sh /entrypoint.sh

RUN         apt update -y && \
            apt upgrade -y && \
            apt install -y gpg wget lsb-release && \
            wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
            gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint && \
            echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list && \
            apt update -y && \
            apt install -y vault && \
            chmod +x /entrypoint.sh && \
            vault server -dev

ENTRYPOINT  ["./entrypoint.sh"]