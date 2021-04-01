"""
    The app.py file will hold all the active endpoints
    for the application and will pose calls to the proper
    functions for each URL.
"""
from perlemir_api.config import config
from perlemir_api.user import user_fun
from perlemir_api.bot import bot_fun
import json

if config.DEBUG:
    print("DEBUG IS ON")

# create the Flask app
app = config.Flask(__name__)
app.secret_key = 'ACM_PERLEMIR_TEST'


#*********************************************************
#                      USER ENDPOINTS
#*********************************************************


@app.route('/api/v1/user/user_get_nonce', methods=['GET'])
def user_get_nonce():
    return user_fun.nonce(config.request)


@app.route('/api/v1/user/user_login', methods=['POST'])
def user_login():
    return user_fun.login(config.request)

@app.route('/api/v1/user/user_logout', methods=['POST'])
def user_logout():
    config.session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/api/v1/user/user_get_settings', methods=['POST'])
def user_get_settings():
    return "d"

@app.route('/api/v1/user/user_change_settings', methods=['POST'])
def user_change_settings():
    return "d"

#*********************************************************
#                      BOT ENDPOINTS
#*********************************************************

@app.route('/api/v1/bot', methods=['GET'])
def get_bots(): 
    return bot_fun.get_bots()

@app.route('/api/v1/bot', methods=['POST'])
def create_bot():
    return bot_fun.create_bot(config.request)

@app.route('/api/v1/bot/<id>', methods=['GET'])
def get_bot(id):
    return bot_fun.get_bot(id)

# @app.route('/api/v1/bot/<id>/get_settings', methods=['GET'])
# def get_settings(id):
#     return bot_fun.get_settings(config.request)



#*********************************************************
#                      TEST ENDPOINT
#*********************************************************
@app.route('/api/v1/generate_key', methods=['POST'])
def test(): 
    return config.aux.respond_generate_key('ladair', 'pwd', 'basic')

@app.route('/api/v1/validate_key', methods=['POST'])
def fun(): 
    return config.aux.validate_key(config.request)

#run the program
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
 
