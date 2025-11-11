# 🌀 StreamStore — Order Event Streaming with Apache Kafka

StreamStore is a lightweight event streaming demo project built with **Apache Kafka** running in **KRaft mode** (no Zookeeper), using **Docker Compose**.  
It includes a Python **Producer** that publishes order events and a **Consumer (Tracker)** that listens and processes these events in real time.

---

## 🧱 Project Structure

streamstore/
├── docker-compose.yaml
├── producer.py
└── tracker.py

---

## ⚙️ Requirements

- **Docker** and **Docker Compose**
- **Python 3.8+**
- **confluent-kafka** Python client

Install the Kafka client library:

```bash
pip install confluent-kafka
```


## Setup

1. **Clone the repository**

``` bash
git clone https://github.com/madhumitta-15/kafka_streamDemo.git
cd kafka_streamDemo
```
2. **Install dependencies**

```bash
pip install confluent-kafka
```

3. **Start Kafka using Docker Compose**

```bash
docker compose up -d
```

## Usage

1. **Run the consumer** (in one terminal):
```bash
python tracker.py
```
2. **Run the producer** (in another terminal):
```bash
python producer.py
```

## Files

- `producer.py`: Sends order messages to Kafka.
- `tracker.py`: Consumes and prints order messages.
- `docker-compose.yml`: Kafka broker setup.

## Notes

- The Kafka topic `orders` is created automatically.
- Make sure Kafka is running before starting the producer or consumer.
