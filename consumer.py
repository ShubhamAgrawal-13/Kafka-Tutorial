from kafka import KafkaConsumer
from sys import argv
import os
import json

def main():
    if(len(argv)<=1):
        print("Enter a topic name first using command line arguments")
        os._exit(0)

    topic = argv[1]
    consumer = KafkaConsumer(topic,
         bootstrap_servers=['localhost:9092'],
         auto_offset_reset='latest',
         enable_auto_commit=True,
         value_deserializer=lambda x: x.decode('utf-8')) # json.loads(x.decode('utf-8'))

    print("[Consumer] Started")
    for msg in consumer:
        print(msg.value)
        if(msg.value == "exit"):
            break

    print("[Consumer] Stopped")


if __name__ == '__main__':
    main()
