"""
    Author:     Lane Adair (ladair@unca.edu)
    Date:       March 5, 2020
    Version:    0.0.1
"""
import json
from perlemir_api.config import config
import uuid

#An associative array containing the bots. The key to the bot is given by the uuid.
bot_list = {}

def name_bot(request):
    return 200

def create_bot(request):
    #check if all fields are filled out, if not then we will return a 206 status
    # bot = config.perlemirBot()
    request_json = request.get_json()

    #if token and key are invalid, do not continue and return 401
    

    bot = {}
    example_uuid = "330b6732-bb2f-4f18-82af-fc5d272139cd"

    if 'name' not in request_json:
        #set the name to "Bot #__" and however many bots there are.
        num = len(bot_list)
        bot['name'] = "Bot # d%" % num
    else:
        bot['name'] = request_json['name']

    if 'strategy' not in request_json:
        #if the stragegy is not included, we will default to dollar-cost-average
        bot['strategy'] = 'dollar-cost-average'
    else:
        bot['strategy'] = request_json['strategy']

    if 'period' not in request_json:
        #if the period is not included, default to weekly
        bot['period'] = 'weekly'
    else:
        bot['period'] = request_json['period']

    if 'frequency' not in request_json:
        #if the frequency does not exist, default to 2
        bot['frequency'] = 2
    else:
        bot['frequency'] = request_json['frequency']

    if 'status' not in request_json:
        #if the status does not exist, default to active
        bot['status'] = 'active'
    else:
        bot['status'] = request_json['status']


    #add the new bot to the bot_list
    bot_list[example_uuid] = bot
    print(bot_list[example_uuid])


    if config.DEBUG:
        return {"uuid" : "330b6732-bb2f-4f18-82af-fc5d272139cd", 
                "name" : bot['name'],
                "status" : bot['status']}, 201     
    else:
        return 201

"""
    Given the bot UUID, we want to kill that bot and remove
    it from the bot list. We should return the HTTP Status code
    of 200.
"""
def pop_bot(request):
    return 200

def get_bots():
    if config.DEBUG:
        print("Queried Bots")
        return bot_list, 200  
    else:
        if bot_list == null:
            return {'message' : 'No bots are found!'}, 404
        else:
            bot_json = json.dumps(bot_list)

            return {'message' : 'Request timed out. Please reload page!'}, 200

def get_bot(id):
    if id not in bot_list:
        return {'message' : 'UUID not found'}, 404
    else:
        return bot_list[id], 200

def test(request):
    return request.get_json()