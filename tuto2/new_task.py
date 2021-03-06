import pika
import sys


message = ' '.join(sys.argv[1:]) or "Hello World!"
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_publish(
    exchange='',
    routing_key='task_queue',  # Queue declared.
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # Make message persistent.
    ),
)
print "[x] Sent %r" % message
connection.close()
