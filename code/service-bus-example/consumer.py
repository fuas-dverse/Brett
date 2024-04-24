import asyncio
from azure.servicebus.aio import ServiceBusClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("CONNECTION_STRING")
queue_name = "test"


async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
            conn_str=connection_string,
            logging_enable=True) as servicebus_client:
        async with servicebus_client:
            while True:
                # get the Queue Receiver object for the queue
                receiver = servicebus_client.get_queue_receiver(queue_name=queue_name)
                async with receiver:
                    received_msgs = await receiver.receive_messages(max_message_count=20)
                    for msg in received_msgs:
                        print("Received: " + str(msg))
                        # complete the message so that the message is removed from the queue
                        await receiver.complete_message(msg)


asyncio.run(run())
