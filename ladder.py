import json

with open('test_ladder.json') as f:
    data = json.load(f)

for i in data['ladder']['entries'][0:10]:
    print(i['character']['name'])
    print(i['character']['realm']['slug'])
    print(i['faction']['type'])
    print('rank:', i['rank'])
    print('rating:', i['rating'])
    print('played:', i['season_match_statistics']['played'])
    print('won:', i['season_match_statistics']['won'])
    print('lost:', i['season_match_statistics']['lost'])
    print('______________________________')
