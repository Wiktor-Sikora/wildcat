import openai
import os 
import json
from dotenv import load_dotenv

def open_ai_completion(description):
    openai.api_key = os.getenv('OPENAI_KEY', None)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant that returns json {"tags": [...], "missing_parts": [...]}'},
            {'role': 'user', 'content': 'it\'s a watch, it shows what time it is. This watch is missing a band'},
            {'role': 'assistant', 'content': '{"tags": ["watch", "clock", "time", "timer", "ticker"], "missing_parts": ["band", "armband", "armlet"]}'},
            {'role': 'user', 'content': description}
        ],
        max_tokens=200,
        temperature=0.2
    )
    tags = json.loads(response['choices'][0]['message']['content']).get('tags', [])
    needs = json.loads(response['choices'][0]['message']['content']).get('missing_parts', [])
    
    return tags, needs
