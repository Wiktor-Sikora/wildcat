import openai, os, json
import os
import json
from dotenv import load_dotenv

def open_ai_completion(description):
    openai.api_key = os.getenv("OPENAI_KEY", None)
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = '(Return json, be cautious abount "needs", example:{"tags":["tags"],"needs":["things"})' + description,
        stop='.',
        max_tokens = 200,
        temperature=0.5
    )
    tags = json.loads(response["choices"][0]["text"]).get("tags", [])
    needs = json.loads(response["choices"][0]["text"]).get("needs", [])
    return tags, needs
