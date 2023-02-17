# Local Kafka Broker

A dockerized Kafka broker with just one node to easily test Kafka integrations locally.

This implementation is based on [@Boyu1997](https://www.github.com/Boyu1997) post: [Intro to Kafka](https://dev.to/boyu1997/intro-to-kafka-4hn2).

## Tech Stack

**Broker:** [Kafka](https://kafka.apache.org/documentation/), [Zookeper](https://kafka.apache.org/documentation/#zk), [Kafdrop](https://github.com/obsidiandynamics/kafdrop), [DockerCompose](https://docs.docker.com/compose/)

**Client:** [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python)

## Features

- Dockerized Kafka broker with zookeeper and one node.
- Dockerized Kafka web UI with kafdrop.
- Test consumer and producer using confluent-kafka library for python.

## Run Locally

Clone the project

```bash
  git clone https://github.com/alanmvarela/local_kafka_broker.git
```

Go to the project directory

```bash
  cd local_kafka_broker
```

Start containers

```bash
  docker-compose up -d
```

Check that the 3 containers for the Zookeeper, Kafka and kafdrop are running

```bash
  docker ps
```

## Stop Broker

To stop the broker run

```bash
  docker-compose stop
```

The clean up the previous execution data with command below if you want a fresh start on the next run.

```bash
  rm -rf data
```

## Running Tests

To test the broker you can use the clients to produce and consumer some mock messages

First open the UI in your browser using below URL and create `test_topic` topic

```bash
  http://localhost:9000/
```

Run producer script to generate 10 new messages for `test_topic` topic. After running this script you should be able to see the new messages within the topic in the UI.

```bash
  python3 client/python/producer.py
```

Run consumer script to consume all messages queued for `test_topic` topic. After runnign this script you should be able to see that all messages within the topic in the UI had dissapeared.

```bash
  python3 client/python/consumer.py
```

## Project Structure

```bash
.
├── client
│   └── python
│       ├── consumer.py
│       └── producer.py
├── docker-compose.yml
├── LICENSE
└── README.md
```

## Lessons Learned

I learnt how to dockerize and use a local instance of Zookeper, Kafka and Kafdrop UI.

Also I was able to provide implementations a basic producer and consumer in python.

## Roadmap

- Add client in Golang.

## Authors

- [@alanmvarela](https://www.github.com/alanmvarela)
