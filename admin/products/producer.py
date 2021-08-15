import pika, json

params = pika.URLParameters('amqps://pnajbiae:iAV3jpzowG9RzB7kmnBjmYZHP8HnWXqa@gerbil.rmq.cloudamqp.com/pnajbiae')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='', 
        routing_key='main', 
        body=json.dumps(body),
        properties=properties
    )