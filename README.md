# Kafka Commands:
-----------------------------------------------------------------------------
#### Note: Before running any command, First move from current directory to the kafka directory.

### 1. To start the Zookeeper Server

##### For windows:
```
.\bin\windows\zookeeper-server-start.bat config\zookeeper.properties
```

##### For linux:
```
.\bin\zookeeper-server-start.sh config\zookeeper.properties
```


### 2. To start the Kafka server

##### For windows:
```
.\bin\windows\kafka-server-start.bat config\server.properties
```

##### For linux:
```
.\bin\kafka-server-start.sh config\server.properties
```

### 3. To create a Topic

##### For windows:
```
.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

##### For linux:
```
.\bin\kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

### 4. To list the Topics

##### For windows:
```
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

##### For linux:
```
.\bin\kafka-topics.sh --list --bootstrap-server localhost:9092
```

### 5. To run the Console Producer

##### For windows:
```
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic test
```

##### For linux:
```
.\bin\kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

### 6. To run the Console Consumer

##### For windows:
```
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning
```

##### For linux:
```
.\bin\kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```
------------------------------------------------------------------------------

