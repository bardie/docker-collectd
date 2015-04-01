FROM debian:jessie

RUN apt-get update && apt-get -y install \
    collectd \
    python \
    python-pip
RUN apt-get clean
RUN pip install docker-py

ADD dockerplugin.py /opt/dockerplugin.py
ADD dockerplugin.db /opt/dockerplugin.db
ADD stat.py /opt/stat.py

CMD ["/usr/sbin/collectd","-f"]
