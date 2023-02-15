from confluent_kafka import Consumer, KafkaError

#Constant to set Bootstrap Server
BOOTSTRAP_SERVERS = 'localhost:9091'
#Constant that defines the topic to subscribe to
TOPIC = 'test_topic'


c = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': 'test-group',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
})

try:
    c.subscribe([TOPIC])
    print("Consumer subscribed to topic: "+str(c.memberid()))
    print("Starting consuming from Kafka Local Broker")
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print("Message pulled succesfully with value: %s", msg.value())
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print("End of partition reached")
        else:
            print("Error")
finally:
        # Close down consumer to commit final offsets.
        c.close()