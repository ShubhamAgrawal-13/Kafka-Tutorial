from kafka import KafkaProducer
from sys import argv
import os
import json

producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

def send_message(topic, msg):
	producer.send(topic, msg.encode('utf-8'))
	#producer.send(topic, json.dumps(dict_msg).encode('utf-8'))


def main():
	if(len(argv)<=1):
		print("Enter a topic name first using command line arguments")
		os._exit(0)

	topic = argv[1]
	print("[Producer] Started")
	while(1):
		data = input("> ")
		send_message(topic, data)
		if(data == "exit"):
			break

	print("[Producer] Stopped")

if __name__ == '__main__':
	main()