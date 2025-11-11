import json
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",  # unique string identifies consumer group to which this consumer belongs
    "auto.offset.reset": "earliest"  # what to do when there is no initial offset or current offset doesn’t exist
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])

print("Consumer is running and subscribed to the 'orders' topic")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error occurred: {msg.error()}")
        continue

    value = msg.value().decode("utf-8")
    order = json.loads(value)  # string to JSON/dictionary
    print(f"Received order: {order['quantity']} x {order['item']} from {order['user']}")
