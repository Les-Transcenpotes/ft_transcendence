FROM debian:bookworm

RUN apt update -y
RUN apt upgrade -y

RUN apt-get install -y apache2 apache2-utils
RUN service apache2 start

EXPOSE 2000

RUN apt install -y libapache2-mod-security2
RUN service apache2 restart
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf
RUN service apache2 restart

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]