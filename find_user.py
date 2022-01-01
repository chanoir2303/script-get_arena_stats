import json

with open('test_ladder.json') as f:
    data = json.load(f)


for i in data['ladder']['entries']:
    if 'Raíku' in data['ladder']['entries'][0]['character']['name']:
        print('ok')
