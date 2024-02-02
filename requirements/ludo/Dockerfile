#---- base image ------------------------------------------------------#

FROM        python:3.12-bookworm

#---- env variables ---------------------------------------------------#

ENV         PYTHONDONTWRITEBYTECODE 1
ENV         PYTHONUNBUFFERED 1

#---- working directory -----------------------------------------------#

WORKDIR     /app

#---- dependencies & requirements -------------------------------------#

COPY        requirements.txt /app/
COPY        ludo_project /app/
RUN         pip install --upgrade pip && \
            pip install --no-cache-dir -r requirements.txt
RUN         apt-get update -y && \
            apt-get upgrade -y && \
            apt-get install apache2 -y && \
            apt-get install libapache2-mod-wsgi-py3 -y

#---- ports -----------------------------------------------------------#

EXPOSE      8000

#---- script ----------------------------------------------------------#

COPY        tools/script.sh /etc/ludo/script.sh
RUN         chmod +x /etc/ludo/script.sh
ENTRYPOINT  ["sh", "/etc/ludo/script.sh"]
