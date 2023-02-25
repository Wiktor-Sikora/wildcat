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
        prompt = prompt + '. Polecenie: Napisz przetlumaczone na angielski tagi z malymi literami. Masz napisac tylko tagi. Przyklad: sell, car, new',
        stop='.',
        max_tokens = 150,
        temperature=0
    )
    print(response)
    data = response["choices"][0]["text"].strip().split(', ')
    return data

