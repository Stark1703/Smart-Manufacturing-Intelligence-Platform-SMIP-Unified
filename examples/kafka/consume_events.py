from streaming.kafka.consumer import ManufacturingKafkaConsumer
from streaming.kafka.topics import MANUFACTURING_EVENTS_TOPIC


def main() -> None:
    consumer = ManufacturingKafkaConsumer()
    consumer.subscribe(MANUFACTURING_EVENTS_TOPIC)
    print("Waiting for messages. Press Ctrl+C to stop.\n")

    try:
        while True:
            message = consumer.poll()
            if message is None:
                continue
            if message.error():
                print(message.error())
                continue

            print("Topic :", message.topic())
            print("Key   :", message.key().decode())
            print("Value :", message.value().decode())
            print("-" * 80)
    except KeyboardInterrupt:
        print("\nConsumer stopped.")


if __name__ == "__main__":
    main()
