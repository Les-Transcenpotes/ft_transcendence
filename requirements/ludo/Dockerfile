#---- base image ------------------------------------------------------#

FROM        python:3.12-bookworm

#---- env variables ---------------------------------------------------#

ENV         PYTHONDONTWRITEBYTECODE 1
ENV         PYTHONUNBUFFERED 1

#---- working directory -----------------------------------------------#

WORKDIR     /app

#---- dependencies & requirements -------------------------------------#

COPY        requirements.txt /app/
RUN         pip install --upgrade pip && \
            pip install --no-cache-dir -r requirements.txt && \
            python -m pip install -U channels["daphne"] && \
            python -m pip install channels_redis

#---- script ----------------------------------------------------------#

COPY        --chmod=+x tools/script.sh /etc/ludo/script.sh

ENTRYPOINT  ["sh", "/etc/ludo/script.sh"]
