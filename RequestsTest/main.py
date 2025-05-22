import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd30e3460d9c2e4da687b81a06d121a30'
HEADER = {'Conten-type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())

pokemon_id = response_create.json()['id']

body_edit = {
    "pokemon_id": pokemon_id,
    "name": "Mewtwo",
    "photo_id": 150
}

response_edit = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit)
print(response_edit.json())

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_edit)
print(response_catch.json())

