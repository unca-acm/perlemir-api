import json
from config import config
#*********************************************************
#                   USER LOGIN FUNCTIONS
#*********************************************************

"""
    On load, the login page should send out a GET request for a nonce generation.
    The nonce will last until for a few minutes to allow the user to login. 

    There is an 'auth' key in the payload, which tells the server that this token is
    only authorized for logging into the services.

    The nonce remains valid for 10 minutes.
"""
def nonce(request):
    try:
        payload = {
            'exp': config.datetime.utcnow() + config.timedelta(seconds=600),
            'iat': config.datetime.utcnow(),
            'auth': 'login'
        }

        return config.jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM), config.status.HTTP_200_OK
    except Exception as e:
        return e, config.status.HTTP_500_INTERNAL_SERVER_ERROR


"""
    The user_login endpoint takes in json data and checks for a nonce, if the nonce
    is valid and authorized for logging in, then allow logging in if username and
    password checkout.
"""
def login(request):
    #take in the request information
    data = request.get_json()

    #check if the user has a valid nonce token
    try:
        nonce = config.aux.decode_token(data['nonce'])

        if config.aux.validate_token(nonce, 'login') == False:
            return {'message' : 'Unauthorized token.'}, 401

        #IF the user exists, check the password
        if checkUID(data['uid']):
            print("Username " + data['uid'] + " matches")

            #check the user's password
            if checkPWD(data['pwd']):
                print("Password for user " + data['uid'] + " matches")
            else:
                print("Password for user " + data['uid'] + " does not match")
                return { 'message' : 'Password incorrect'}, 403
        else:
            print("Username " + data['uid'] + " does not match")
            return { 'message' : 'Username incorrect!'}, 404

        payload = {
            'uid': data['uid'],
            'exp': config.datetime.utcnow() + config.timedelta(seconds=1800),
            'auth': 'standard'
        }

        jwt_token = config.jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM)

        retJSON = {
            'uid' : data['uid'],
            'session-token' : jwt_token        
        }

        #The last step of a successful login is creating a session.
        config.session['uid'] = data['uid']
        
        if config.DEBUG:
            print("session created with username: " + config.session['uid'])

        return retJSON, config.status.HTTP_200_OK
    except Exception as e:
        if config.DEBUG:
            print("NONCE EXPIRED")
        return {'message' : 'Request timed out. Please reload page to obtain new nonce!'}, 205

def extract_json(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr
    
    values = extract(obj, arr, key)
    return values

def checkUID(uName):
    #check if we should use the testUser function
    if not config.DEBUG:
        if uName == queryName(uName):
            return True
    else:
        f = open(config.UD_FILE)
        data = json.load(f)
        f.close()
        
        if data['user']['name'] == uName:
            return True

    #if neither applies, then return false
    return False
#end checkUID(String)

def checkPWD(pwd):
    if not config.DEBUG:
        return True
    else:
        f = open(config.UD_FILE)
        data = json.load(f)
        f.close()

        if data['user']['pwd'] == pwd:
            return True
            
    return False
#end checkPWD()

def testUser():
    tf = open("../ud/ladair", "r")
    u = tf.readline()
    tf.close()

    return u
#end testUser()

def testPWD():
    tf = open("../ud/ladair", "r")
    tf.readline()
    pwd = tf.readline()
    tf.close()

    return pwd
#end testPWD

def queryUser(uName):
    print("test")
#end queryUser()

#*********************************************************
#                   USER LOGOUT FUNCTIONS
#*********************************************************
def logout(request):
    print("LOGOUT")
    sess

#*********************************************************
#                   USER CREATION FUNCTIONS
#*********************************************************
def createUID():
    print("UID")

#end createUID

#*********************************************************
#                   USER DELETION FUNCTIONS
#*********************************************************


#*********************************************************
#                   USER SETTINGS FUNCTIONS
#*********************************************************
