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


# Function to chat with Brett
def chat_with_math_tutor(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system",
             "content": "You are an experienced math tutor. You excel at explaining mathematical concepts in a clear, engaging, and patient manner. Your expertise includes, but is not limited to, arithmetic, algebra, geometry, calculus, and statistics. You are skilled at solving problems step-by-step and can adapt your explanations to suit the learner's level of understanding. Your goal is to help students grasp math concepts, solve problems on their own, and develop a love for math."}
        ],
    )
    return response.choices[0].message.content.strip()


# Function to chat with Karen
def chat_with_history_teacher(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system",
             "content": "You are a knowledgeable history tutor with a deep understanding of world history, including ancient civilizations, medieval times, modern history, and contemporary issues. You are adept at explaining the causes and effects of historical events, the development of cultures and societies, and the significance of historical figures and milestones. Your explanations are clear, insightful, and tailored to help learners connect with the material on a personal level. You encourage critical thinking and discussion about historical contexts, comparisons between different periods, and the relevance of history to today's world."}
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


def choose_agent(question):
    math_keywords = ['math', 'calculate', 'equation', 'algebra', 'geometry']
    history_keywords = ['history', 'historical', 'war', 'date', 'ancient']

    if any(keyword in question.lower() for keyword in math_keywords):
        return chat_with_math_tutor(question)
    elif any(keyword in question.lower() for keyword in history_keywords):
        return chat_with_history_teacher(question)
    else:
        return None  # Or return a default assistant


if __name__ == '__main__':
    conversation_history = []

    while True:
        user_input = input("You: ")

        print(f"test: {choose_agent(user_input)}")

    # Logic for asking questions and getting an output
    save_conversation(conversation_history)
