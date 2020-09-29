FROM pypy:3-6
RUN mkdir -p /usr/api/logs
WORKDIR /usr/api
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get --allow-unauthenticated install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY ./deployment/gunicorn.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /usr/api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3000
VOLUME /usr/api
CMD ["/usr/bin/supervisord"]