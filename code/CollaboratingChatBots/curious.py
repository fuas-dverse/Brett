import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
assistant_id = "asst_N5h8brhzcZenDzTV4WhihFTp"

# # Create a Math Tutor assistant
# assistant = client.beta.assistants.create(
#     name="Math Tutor",
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-turbo-preview",
# )

thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Solve this problem: 3x + 11 = 14"
        }
    ]
)

run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"Run Status: {run.status}")
    time.sleep(1)
else:
    print("Run Completed")


message_response = client.beta.threads.messages.list(
    thread_id=thread.id,
)
messages = message_response.data


latest_message = messages[0]
print(f"Response: {latest_message.content[0].text.value}")