import time
import pika
import logging
from .config import *

class Rabbit_base:
    def __init__(self, message: str = None, queue_=None):
        self.credentials = pika.PlainCredentials(username=RABBITMQ_LOGIN, password=RABBITMQ_PASSWORD)
        self.parameters = pika.ConnectionParameters(host=RABBITMQ_IP, port=RABBITMQ_PORT, virtual_host='/',
                                                    credentials=self.credentials)
        self.connection = None
        self.channel = None
        self.message = message
        self.queue = queue_

    def connect(self):
        try:
            if not self.connection or self.connection.is_closed:
                self.connection = pika.BlockingConnection(self.parameters)
                self.channel = self.connection.channel()
                if self.connection:
                    return self.connection

        except pika.exceptions.AMQPConnectionError as error:
            time.sleep(3)
            self.connect()

        except pika.exceptions.ConnectionClosedByBroker as error:
            time.sleep(3)
            self.connect()

        except pika.exceptions.ConnectionWrongStateError as error:
            time.sleep(3)
            self.connect()


class Rabbit_sender(Rabbit_base):
    def send_message(self):
        self.connect()
        if self.connection:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue, body=self.message)
