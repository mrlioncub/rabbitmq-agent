# rabbitmq-agent
[![Build Status](https://img.shields.io/docker/cloud/build/mrlioncub/rabbitmq-agent)](https://hub.docker.com/r/mrlioncub/rabbitmq-agent)
[![Docker Automated build](https://img.shields.io/docker/cloud/automated/mrlioncub/rabbitmq-agent)](https://hub.docker.com/r/mrlioncub/rabbitmq-agent)
[![Docker Image Size](https://img.shields.io/docker/image-size/mrlioncub/rabbitmq-agent/latest)](https://hub.docker.com/r/mrlioncub/rabbitmq-agent)

Sender and reciever messages for RabbitMQ

# How to use this image
## Example
  1. Run RabbitMQ:
```
docker run --rm -d -p 15672:15672 --name rabbitmq-server rabbitmq:management-alpine
```
  2. Run Reciever:
```
docker run --rm --link rabbitmq-server:rabbitmq-server mrlioncub/rabbitmq-agent reciever
```
  3. Run Sender (send 10 messages):
```
docker run --rm --link rabbitmq-server:rabbitmq-server mrlioncub/rabbitmq-agent sender 10
```
## Environment variables
If you wish to change the default username, password or hosname to connect rabbitmq server, you can do so with environmental variables:
  - RABBITMQ_USER
    (default username 'guest')
  - RABBITMQ_PASS
    (default password 'guest')
  - RABBITMQ_HOST
    (default hostname 'rabbitmq_server')

## Links
  - RabbitMQ Tutorials (https://www.rabbitmq.com/getstarted.html)
  - RabbitMQ-Samples (https://github.com/ryan-a-baker/k8s-scaling-demo/tree/master/RabbitMQ-Samples)
