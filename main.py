from blizzardapi import BlizzardApi
import json

api_client = BlizzardApi("client_id", "client_secret")

# Unprotected API endpoint
categories_index = api_client.wow.game_data.get_achievement_categories_index("us", "en_US")

# Wow Classic endpoint
connected_realms_index = api_client.wow.game_data.get_connected_realms_index("us", "en_US", is_classic=True)

y = api_client.wow.game_data.get_pvp_leaderboard('eu', 'en_EU', 27, '3v3')

x = open('test_ladder.json', 'a+')
x.write(json.dumps({'ladder': y}))
x.close()



