#---- base image ------------------------------------------------------#

FROM    logstash:8.12.2

#---- configuration files ---------------------------------------------#

RUN     rm -f   /usr/share/logstash/pipeline/logstash.conf
COPY    pipeline/   /usr/share/logstash/pipeline/
COPY    config/   /usr/share/logstash/config/