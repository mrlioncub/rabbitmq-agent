#!/usr/bin/env python

import pika
import os
import sys
import random

credentials = pika.PlainCredentials(os.environ['RABBITMQ_USER'],os.environ['RABBITMQ_PASS'])
connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST'],credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

for x in range(int(sys.argv[1])):
    message="Message #" + str(x)
    for y in range(1,random.randint(2,10)):
        message=message + "."

    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode = 2,
                          ))
    print(" [x] Sent %r" % message)

connection.close()
