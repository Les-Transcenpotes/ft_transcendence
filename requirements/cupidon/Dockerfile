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

#---- script ----------------------------------------------------------#

COPY        --chmod=+x tools/script.sh /etc/cupidon/script.sh

ENTRYPOINT  ["sh", "/etc/cupidon/script.sh"]
