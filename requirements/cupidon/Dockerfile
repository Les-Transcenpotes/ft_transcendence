FROM        python:3.12-bookworm

ENV         PYTHONDONTWRITEBYTECODE 1
ENV         PYTHONUNBUFFERED 1

WORKDIR     /app

COPY        requirements.txt /app/
RUN         pip install --upgrade pip
RUN         pip install --no-cache-dir -r requirements.txt
RUN         pip install gunicorn

EXPOSE      8000

COPY        tools/script.sh /etc/cupidon/script.sh
RUN         chmod +x /etc/cupidon/script.sh
ENTRYPOINT  ["sh", "/etc/cupidon/script.sh"]
