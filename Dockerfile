FROM debian:jessie

RUN apt-get update && apt-get -y install \
    collectd \
    python \
    python-pip
RUN pip install docker-py

ADD dockerplugin.py /opt/dockerplugin.py
ADD dockerplugin.db /opt/dockerplugin.db

CMD ["/usr/sbin/collectd -f"]
