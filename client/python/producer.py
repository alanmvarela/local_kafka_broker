from confluent_kafka import Producer

#Constant to set Bootstrap Server
BOOTSTRAP_SERVERS = 'localhost:9091'
#Constant that defines the topic to write to
TOPIC = 'test_topic'
#Constant that defines the key to which partition to write to
KEY = 'hello'

p = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

#Produces 10 messages to the selected topic and key
for data in range(10):
    p.produce(TOPIC, key=KEY, value=str(data))
p.flush(30)
