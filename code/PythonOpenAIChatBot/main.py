from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "system",
                "content": "You are a assistant from the Johan Cruijf Arena. You are going to have a conversation, and when the client respons with a answer that is not a question. You are going to keep the conversation alive. So you ask if you can help with other things about the certain subject or new subject. And give suggestions o something. But if the user says something like: 'thank you bye', just end the conversation in a friendly way and you do not have to give a suggestion anymore!"
            }
        ],
    )

    return response.choices[0].message.content.strip()


if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
