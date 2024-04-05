from confluent_kafka import Consumer, KafkaError, KafkaException

c = Consumer({
    'bootstrap.servers': '127.0.0.1:8080',
    'group.id': 'breno',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['test_topic'])

try:
    while True:
        msg = c.poll(1.0)  # wait for a message up to 1 second
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print('Received message: {}'.format(msg.value().decode('utf-8')))
finally:
    # Clean up on exit
    c.close()



