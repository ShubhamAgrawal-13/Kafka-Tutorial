from kafka import KafkaProducer
from sys import argv
import os
import json

def send_message(topic, msg):
	producer.send(topic, msg.encode('utf-8'))
	#producer.send(topic, json.dumps(dict_msg).encode('utf-8'))


def main():
	if(len(argv)<=1):
		print("enter topic")
		os._exit(0)

	producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
	topic = argv[1]
	while(1):
		data = input("> ")
		send_message(topic, data)

if __name__ == '__main__':
	main()