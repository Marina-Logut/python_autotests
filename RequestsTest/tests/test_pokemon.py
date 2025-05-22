import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd30e3460d9c2e4da687b81a06d121a30'
HEADER = {'Conten-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 33743

def test_status_code():
    response = requests.get(url = f'{URL}/trainers/{TRAINER_ID}')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers/{TRAINER_ID}')
    assert response.json()['trainer_name'] == 'Morti'