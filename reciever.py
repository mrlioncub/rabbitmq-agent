#!/usr/bin/env python

import pika
import os
import time

credentials = pika.PlainCredentials(os.environ['RABBITMQ_USER'],os.environ['RABBITMQ_PASS'])
connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST'],credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body, end=' ')
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" done [x]")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
