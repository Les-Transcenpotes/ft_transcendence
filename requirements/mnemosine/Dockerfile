#---- base image ------------------------------------------------------#

FROM        python:3.12-bookworm

#---- env variables ---------------------------------------------------#

ENV         PYTHONDONTWRITEBYTECODE 1
ENV         PYTHONUNBUFFERED 1

#---- working directory -----------------------------------------------#

WORKDIR     /app

#---- dependencies & requirements -------------------------------------#

COPY        requirements.txt /app/
COPY        mnemosine_project /app/
RUN         pip install --upgrade pip && \
            pip install --no-cache-dir -r requirements.txt
RUN         apt-get update -y && \
            apt-get upgrade -y && \
            apt-get install apache2 -y && \
            apt-get install libapache2-mod-wsgi-py3 -y

#---- ports -----------------------------------------------------------#

EXPOSE      8000

#---- script ----------------------------------------------------------#

COPY        tools/script.sh /etc/mnemosine/script.sh
RUN         chmod +x /etc/mnemosine/script.sh
ENTRYPOINT  ["sh", "/etc/mnemosine/script.sh"]
# CMD         ["/bin/bash"] #debug if launch line does not work
