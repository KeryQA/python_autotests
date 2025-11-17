import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ede95c389942f357f3ae22560b95bae5'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '42646'

def test_status_code():
    responce = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_responce():
    responce_get = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert responce_get.json()['data'][0]['id'] == '42646'