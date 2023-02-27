from django.shortcuts import render
import openai, os, json
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_KEY", None)

def tager(input):
    openai.api_key = key
    prompt = input
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt + ' (Return json, example:{"tags":["category", "things"],"need":["things"})',
        stop='.',
        max_tokens = 150,
        temperature=0.5
    )
    print(response)
    data = json.loads(response["choices"][0]["text"])
    print(data)
    
    return data
