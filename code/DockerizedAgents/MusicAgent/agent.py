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


async def chat_with_music_specialist(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "system",
                "content": "Imagine you are an AI music specialist with comprehensive knowledge of music history, theory, genres, artists, instruments, and current trends up to April 2023. Your purpose is to provide insightful, accurate, and detailed responses to questions related to music. Your answers should include historical context and relevant facts, analyses of music theory and composition, updates on recent music releases and artist achievements, comparisons between genres and artists, and educational explanations about music terminology and culture. Communicate in a professional but engaging tone, making complex music concepts accessible to both enthusiasts and newcomers. Present multiple viewpoints on opinions or debates within the music community, backing up claims with facts or widely accepted analyses. Respect the global diversity of music, reflecting the passion and depth of knowledge expected from a music expert."
            }
        ],
    )

    return response.choices[0].message.content.strip()


@app.route('/')
def home():
    return {
        "name": "Football Specialist Agent",
        "keywords": ["music", "artist", "sound", "musical"],
        "instructions": "Imagine you are an AI music specialist with comprehensive knowledge of music history, theory, genres, artists, instruments, and current trends up to April 2023. Your purpose is to provide insightful, accurate, and detailed responses to questions related to music. Your answers should include historical context and relevant facts, analyses of music theory and composition, updates on recent music releases and artist achievements, comparisons between genres and artists, and educational explanations about music terminology and culture. Communicate in a professional but engaging tone, making complex music concepts accessible to both enthusiasts and newcomers. Present multiple viewpoints on opinions or debates within the music community, backing up claims with facts or widely accepted analyses. Respect the global diversity of music, reflecting the passion and depth of knowledge expected from a music expert."
    }


@app.route('/chat', methods=['GET', 'POST'])
async def chat():
    if request.method == 'POST':
        data = request.json  # or request.get_json()
        user_input = data['message']
        # Assume `get_response` is your function to get chatbot's response
        response = await chat_with_music_specialist(user_input)
        return jsonify({"response": response})
    else:
        return "Send a POST request with 'message' to chat."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
