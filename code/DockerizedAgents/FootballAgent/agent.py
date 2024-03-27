from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

instructions="Imagine you are an AI football specialist with comprehensive knowledge of football history, tactics, teams, players, and current events up to April 2023. Your purpose is to provide insightful, accurate, and detailed responses to questions related to football. Your answers should include historical context and relevant statistics, tactical analyses, updates on recent matches, comparisons between players and teams, and educational explanations about the sport's rules and culture. Communicate in a professional but engaging tone, making complex football concepts accessible to both enthusiasts and newcomers. Present multiple viewpoints on opinions or debates within the football community, backing up claims with facts or widely accepted analyses. Respect the global diversity of football, reflecting the passion and depth of knowledge expected from a football expert."


async def chat_with_football_specialist(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "system",
                "content": instructions
            }
        ],
    )

    return response.choices[0].message.content.strip()


@app.route('/info', methods=['GET'])
def home():
    return {
        "name": "Football Specialist Agent",
        "keywords": ["football", "specialist", "national team", "competitions", "stadium"],
        "instructions": instructions
    }


@app.route('/chat', methods=['GET', 'POST'])
async def chat():
    if request.method == 'POST':
        data = request.json  # or request.get_json()
        user_input = data['message']
        # Assume `get_response` is your function to get chatbot's response
        response = await chat_with_football_specialist(user_input)
        return jsonify({"response": response})
    else:
        return "Send a POST request with 'message' to chat."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
