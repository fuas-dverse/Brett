from openai import OpenAI
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure the conversations directory exists
Path("./conversations").mkdir(parents=True, exist_ok=True)

# ANSI escape codes for colors in terminal to read the conversation better
BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'  # Reset to default color

# Function to chat with Brett
def chat_with_gpt_brett(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are Brett. Your goal is to discuss sports with Karen, focusing on soccer. Try to ask engaging questions about soccer teams, matches, and players. If Karen tries to change the subject, politely steer the conversation back to soccer. End the conversation if Karen says goodbye in any form."}
        ],
    )
    return response.choices[0].message.content.strip()

# Function to chat with Karen
def chat_with_gpt_karen(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are Karen. Engage in a conversation about soccer but try to shift the topic to music, specifically discussing various music genres and your favorite songs. If Brett asks about soccer, give a brief answer and then change the subject to music. Say goodbye if the conversation naturally comes to an end or if you run out of things to say about music."}
        ],
    )
    return response.choices[0].message.content.strip()

# Function to save the conversation in a json file inside the "/conversations" folder
def save_conversation(conversation):
    filename = datetime.now().strftime("conversation-%Y-%m-%d-%H-%M-%S.json")
    filepath = os.path.join("./conversations", filename)
    with open(filepath, "w") as file:
        json.dump(conversation, file, indent=4)
    print(f"Conversation saved to {filepath}")


if __name__ == '__main__':
    conversation_history = []
    prompt = "Let's talk about soccer. Do you have a favorite team?"
    iteration = 0
    while iteration < 5:  # Limit to 5 iterations for safety
        brett_msg = f"{BLUE}Brett: {prompt}{ENDC}"
        print(brett_msg)
        conversation_history.append({"Brett": prompt})

        response = chat_with_gpt_karen(prompt)
        karen_msg = f"{RED}Karen: {response}{ENDC}"
        print(karen_msg)
        conversation_history.append({"Karen": response})

        prompt = chat_with_gpt_brett(response)
        iteration += 1

        if "goodbye" in response.lower() or "bye" in response.lower():
            print("Conversation ended.")
            break

    save_conversation(conversation_history)
