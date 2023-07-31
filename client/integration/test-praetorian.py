import json
from confluent_kafka import Producer
from dataclasses import dataclass

# Constant to set Bootstrap Server
BOOTSTRAP_SERVERS = 'localhost:9091'
# Constant that defines the topic to write to
TOPIC = 'test_topic'
# Constant that defines the key to which partition to write to
KEY = 'hello'

p = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})


@dataclass
class KafkaMessageHeader:
    type: str
    productId: str
    projectId: str
    traceId: str
    timeStamp: str
    scannerIp: str
    stages: str
    staticIp: str
    RedTeam: str

@dataclass
class KafkaMessagePayload:
    Platform: str
    Config: str


@dataclass
class KafkaMessage:
    header: KafkaMessageHeader
    payload: KafkaMessagePayload


# Success Message
header = KafkaMessageHeader(
    type="dnsIntegrationEvent",
    productId="11111111-1111-1111-1111-111111111111",
    projectId="11111111-1111-1111-1111-111111111111",
    traceId="test-trace-id",
    timeStamp="2023-01-01T00:00:00.000Z",
    scannerIp="scanner_test",
    stages=["stages_test"],
    staticIp=True,
    RedTeam=True
).__dict__

payload = KafkaMessagePayload(
    Platform="dns/ns1",
    Config="11111111-1111-1111-1111-111111111111"
).__dict__

KafkaMessageOutput = KafkaMessage(
    header=header,
    payload=payload
)

json_payload = json.dumps(KafkaMessageOutput.__dict__)
# # Produces message to the selected topic and key
p.produce(TOPIC, key=KEY, value=json_payload, headers=None)
p.flush(30)

"""
# Error Message - Wrong Platform
payload = KafkaMessagePayload(
    Platform="unexisting platform",
    Config="ns1-integration-nan"
).__dict__

KafkaMessageOutput = KafkaMessage(
    header=header,
    payload=payload
)

json_payload = json.dumps(KafkaMessageOutput.__dict__)
p.produce(TOPIC, key=KEY, value=json_payload, headers=None)


# Error Message - Wrong Config
payload = KafkaMessagePayload(
    Platform="dns/ns1",
    Config="unexisting config"
).__dict__

KafkaMessageOutput = KafkaMessage(
    header=header,
    payload=payload
)

json_payload = json.dumps(KafkaMessageOutput.__dict__)
p.produce(TOPIC, key=KEY, value=json_payload, headers=None)
p.flush(30)
"""