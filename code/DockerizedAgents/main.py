import requests
from pymongo import MongoClient
import re
import asyncio
import aiohttp

client = MongoClient("mongodb://root:example@localhost:27017/")
db = client.dverse_database
collection = db.avialable_agents


def initialize_database():
    collection.delete_many({})

    collection.insert_many(
        [
            {
                "name": "Football Specialist Agent",
                "url": "http://127.0.0.1:5000",
                "keywords": ["football", "specialist", "national team", "competitions", "stadium"],
                "instructions": "Imagine you are an AI football specialist with comprehensive knowledge of football history, tactics, teams, players, and current events up to April 2023. Your purpose is to provide insightful, accurate, and detailed responses to questions related to football. Your answers should include historical context and relevant statistics, tactical analyses, updates on recent matches, comparisons between players and teams, and educational explanations about the sport's rules and culture. Communicate in a professional but engaging tone, making complex football concepts accessible to both enthusiasts and newcomers. Present multiple viewpoints on opinions or debates within the football community, backing up claims with facts or widely accepted analyses. Respect the global diversity of football, reflecting the passion and depth of knowledge expected from a football expert."
            },
            {
                "name": "Music Specialist Agent",
                "url": "http://127.0.0.1:5001",
                "keywords": ["music", "artist", "sound", "musical"],
                "instructions": "Imagine you are an AI music specialist with comprehensive knowledge of music history, theory, genres, artists, instruments, and current trends up to April 2023. Your purpose is to provide insightful, accurate, and detailed responses to questions related to music. Your answers should include historical context and relevant facts, analyses of music theory and composition, updates on recent music releases and artist achievements, comparisons between genres and artists, and educational explanations about music terminology and culture. Communicate in a professional but engaging tone, making complex music concepts accessible to both enthusiasts and newcomers. Present multiple viewpoints on opinions or debates within the music community, backing up claims with facts or widely accepted analyses. Respect the global diversity of music, reflecting the passion and depth of knowledge expected from a music expert."
            }
        ]
    )


# Initialize database with correct data
initialize_database()


def preprocess_text(text):
    """Lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    return text


def find_best_agent(question):
    question = preprocess_text(question)
    best_agent = None
    max_score = 0

    for agent in collection.find({}):
        score = sum(keyword in question for keyword in agent["keywords"])
        if score > max_score:
            max_score = score
            best_agent = agent

    return best_agent


async def fetch_response(url, question):
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{url}/chat", json={"message": question}, headers=headers) as response:
            return await response.json()  # Assuming the API returns JSON


async def ask_question(question):
    best_agent = find_best_agent(question)
    if best_agent:
        response = await fetch_response(best_agent['url'], question)
        print(f"{best_agent['name']}: {response['response']}")
    else:
        print("No suitable agent found.")


if __name__ == '__main__':
    while True:
        question = input(f"You: ")
        asyncio.run(ask_question(question))
