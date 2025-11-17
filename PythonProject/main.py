import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ede95c389942f357f3ae22560b95bae5'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Ronda",
    "photo_id": 629
}
body_update = {
    "pokemon_id": "535789",
    "name": "Rondik"
}
body_in_pokeball = {
    "pokemon_id": "535789"
}

# responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
# print(responce_create.text)

# pokemon_id = responce_create.json()['id']
# print(pokemon_id)

# responce_update = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=body_update)
# print(responce_update.text)

# responce_in_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_in_pokeball)
# print(responce_in_pokeball.text)