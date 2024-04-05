from confluent_kafka import Producer


def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg}")


p = Producer({'bootstrap.servers': '127.0.0.1:8080'})

try:
    p.produce('brett', 'Hello, World!', callback=acked)
    p.flush()
except Exception as e:
    print(f"Exception: {e}")
