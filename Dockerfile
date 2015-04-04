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
ADD docker-stats.py /opt/collectd/bin/docker-stats.py
ADD docker-report.py /opt/collectd/bin/docker-report.py
ADD collectd.conf /etc/collectd/collectd.conf

CMD ["/usr/sbin/collectd","-f"]
