#---- base image ------------------------------------------------------#

FROM    elasticsearch:8.12.2

COPY    config/elasticsearch.yml ./config/elasticsearch.yml
# COPY    config/certificates/* ./config/

# RUN     elasticsearch-certutil cert elasticsearch-certutil cert --pem --in config/certificates --out config/certificates--pem --in config/certificates --out config/certificates
