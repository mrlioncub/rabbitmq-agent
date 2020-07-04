FROM python:3-alpine

ENV RABBITMQ_USER guest
ENV RABBITMQ_PASS guest
ENV RABBITMQ_HOST rabbitmq-server

WORKDIR /data

COPY docker-entrypoint.sh /data
COPY sender.py /data
COPY reciever.py /data

RUN set -x \
  && python -m pip install --no-cache-dir pika --upgrade

ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]
