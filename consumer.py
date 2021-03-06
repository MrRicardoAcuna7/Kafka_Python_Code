import json 
from kafka import KafkaConsumer


if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'
    )
    for message in consumer:
        print(message)