from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_KEY", None)

def tager(input):
    openai.api_key = key
    prompt = input
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt + ' /././ Write translated to eanglish products tags python list with name country this language without launguage name',
        stop='/././',
        max_tokens = 150,
        temperature=0
    )
    print(response)
    data = response["choices"][0]["text"]
    return data