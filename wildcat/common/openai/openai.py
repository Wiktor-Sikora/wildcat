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
        prompt = prompt + '. (Polecenie: Napisz przetlumaczone na angielski tagi malymi literami, na podstawie tekstu dodaj tagi kategori itp. Masz napisac tylko tagi. Przyklad: car, silicon wafer. Nie podawaj podanych tagów: sell, for sale)',
        stop='.',
        max_tokens = 150,
        temperature=0.5
    )
    print(response)
    data = response["choices"][0]["text"].strip().split(', ')
    return data
# (Polecenie: Napisz po angielsku listę produktów z małą dostępnością na świecie, wypisz produkty według przykładu: cobalt, printer, graphic card )
