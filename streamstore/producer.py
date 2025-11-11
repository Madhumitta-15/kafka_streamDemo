import uuid
import json

from confluent_kafka import Producer

producer_config = {'bootstrap.servers':'localhost:9092'}

producer= Producer(producer_config)

def delivery_reports(err ,msg):
    if err:
        print(f" Delivery failed: {err}")
    else:
        print(f" Delivered {msg.value().decode('utf-8')}")
        print(f" Delivered to {msg.topic()}: partition :{msg.partition()} at offset {msg.offset()}")

order ={
    "order_id": str(uuid.uuid4()),
    "user":"chloe",
    "item": "mobile phone",
    "quantity": 2
}

value=json.dumps(order).encode("utf-8")

#kafka create the topic automatically
producer.produce(topic="orders", value=value,callback=delivery_reports) #to know msg is delivered successfully ,track it using the callback function

producer.flush() ##buffer events sends before the program ends


