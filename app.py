"""
    The app.py file will hold all the active endpoints
    for the application and will pose calls to the proper
    functions for each URL.
"""
from perlemir_api.config import config
from perlemir_api.user import user_fun
import json

if config.DEBUG:
    print("DEBUG IS ON")

# create the Flask app
app = config.Flask(__name__)
app.secret_key = 'ACM_PERLEMIR_TEST'


#*********************************************************
#                       ENDPOINTS
#*********************************************************

#This function returns a token that will be used to encrypt the password sent in.
@app.route('/user_get_nonce', methods=['POST'])
def user_get_once():
    try:
        payload = {
            'exp': config.datetime.utcnow() + config.timedelta(seconds=150),
            'iat': config.datetime.utcnow()
        }

        return config.jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM), config.status.HTTP_200_OK
    except Exception as e:
        return e, config.status.HTTP_500_INTERNAL_SERVER_ERROR


"""
    The user_login endpoint takes in json data and checks for a nonce, if the nonce
    is valid, it p
"""
@app.route('/user_login', methods=['POST'])
def user_login():

    #take in the request information
    data = config.request.get_json()

    #check if the user has a valid nonce token
    try:
        nonce = config.jwt.decode(data['nonce'], config.JWT_SECRET, config.JWT_ALGORITHM)
    except Exception as e:
        print("NONCE EXPIRED")
        return {'message' : 'Request timed out. Please reload page!'}, 408



    #IF the user exists, check the password
    if user_fun.checkUID(data['uid']):
        print("Username " + data['uid'] + " matches")

        #check the user's password
        if user_fun.checkPWD(data['pwd']):
            print("Password for user " + data['uid'] + " matches")
        else:
            print("Password for user " + data['uid'] + " does not match")
            return { 'message' : 'Password incorrect'}, 403
    else:
        print("Username " + data['uid'] + " does not match")
        return { 'message' : 'Username incorrect!'}, 404

    payload = {
        'uid': data['uid'],
        'exp': config.datetime.utcnow() + config.timedelta(seconds=1200)
    }

    jwt_token = config.jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM)

    retJSON = {
        'uid' : data['uid'],
        'token' : jwt_token        
    }

    #The last step of a successful login is creating a session.
    config.session['uid'] = data['uid']
    
    if config.DEBUG:
        print("session created with username: " + config.session['uid'])

    return retJSON, config.status.HTTP_200_OK

@app.route('/user_logout', methods=['POST'])
def user_logout():
    config.session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/user_get_settings', methods=['POST'])
def user_get_settings():
    return "d"

@app.route('/user_change_settings', methods=['POST'])
def user_change_settings():
    return "d"

@app.route('/get_price', methods=['POST'])
def get_price():
    return "d"

#run the program
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
 
