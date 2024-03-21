import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

# Load the environment variables
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Assistant IDs
math_assistant = "asst_N5h8brhzcZenDzTV4WhihFTp"  # Assistant for Math
history_assistant = "asst_Fp4q0MCT5n77QI7xFulDRt6q"  # Assistant for History

# User question
user_question = "Can you tell me about world war 2"


# Function to determine the assistant based on keywords
def choose_assistant(question):
    math_keywords = ['math', 'calculate', 'equation', 'algebra', 'geometry']
    history_keywords = ['history', 'historical', 'war', 'date', 'ancient']

    if any(keyword in question.lower() for keyword in math_keywords):
        return math_assistant
    elif any(keyword in question.lower() for keyword in history_keywords):
        return history_assistant
    else:
        return None  # Or return a default assistant


# Choose the assistant based on the question
chosen_assistant = choose_assistant(user_question)

if chosen_assistant is None:
    print("Could not determine the appropriate assistant.")
else:
    # Create a thread for the conversation
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    # Run the thread with the chosen assistant
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=chosen_assistant)

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        print(f"Run Status: {run.status}")
        time.sleep(1)
    else:
        print("Run Completed")

    # Retrieve and print the response
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    latest_message = messages[0]
    print(f"{chosen_assistant}: {latest_message.content[0].text.value}")
