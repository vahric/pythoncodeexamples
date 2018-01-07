
import logging
import pika

# Lets debug everything to the log file
# format add date before message
logging.basicConfig(filename="logs/pika.log",level="DEBUG",format='%(asctime)s %(message)s')

# Provide username and pass , for Openstack check nova.conf for it
credentials = pika.PlainCredentials('rmq_nova_user', '2UhCFjnvHPk')
# Provide ip address of RabbitMQ Server , port , vhost and credentials
connection_parameters = pika.ConnectionParameters('10.111.45.51',5672,'/',credentials)
# Make connection
# Here we are making non-async connection , for async SelectConnection
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Specify queue name, exist or not
channel.queue_declare(queue='notifications.info')

# First need to subscribe and when message received Pika call this callback function to get it.
# %r is repr() function and return valid Python syntax.
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    logging.info('%r' % body)

channel.basic_consume(callback,queue='notifications.info')

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()

# Links https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# Pika documentation http://pika.readthedocs.io/en/0.10.0/index.html
# Logging how-to
# https://books.google.com.tr/books?id=y1MoDwAAQBAJ&pg=PA144&lpg=PA144&dq=queue+name+of+nova+notifications&source=bl&ots=Gt1La88dpa&sig=sBrwZ3tCs2Kvtt9OOj1Yy5M8Cg0&hl=tr&sa=X&ved=0ahUKEwih2YH-5sXYAhUIApoKHWqZAvMQ6AEIczAI#v=onepage&q=queue%20name%20of%20nova%20notifications&f=false
# https://stackoverflow.com/questions/34202345/rabbitmq-def-callbackch-method-properties-body
# https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html
# http://pika.readthedocs.io/en/0.10.0/examples/comparing_publishing_sync_async.html








