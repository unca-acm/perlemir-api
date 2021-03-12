from config import config
import secrets
import base64

def validate_token(token, required_auth):
    #check whether the token has the desired auth type, if token is not valid, or auth type does not match, return false.
    try:
        decoded = config.jwt.decode(token, config.JWT_SECRET, config.JWT_ALGORITHM)

        if decoded['auth'] == required_auth:
            return true
    except Exception as e:
        return false
    return false
#end validate_token

def decode_token(token):
    decoded = config.jwt.decode(token, config.JWT_SECRET, config.JWT_ALGORITHM)
    return decoded
#end decode_token

#Here we have to take in user data from the token and validate by regenerating the API key
#You may have either the token null with uid, pwd, and auth full, or the latter.
def validate_key(request):
    try:
        data = request.get_json()
        key = data['X-API-KEY']

        if 'token' not in data:
            print("Token not present")
            if key == generate_key(data['uid'], data['pwd'], data['auth']):
                print("Keys match")
                return {"X-API-KEY" : key, "message" : "Success"} , 200
            else:
                print("Keys do not match")
                return {"message" : "key not valid"}, 401
        elif 'uid' not in data or 'pwd' not in data or 'auth' not in data:
            if 'token' in data:
                return {"X-API-KEY" : key, "message" : "Success"} , 200
            else:
                return {"message" : "key not valid"}, 401
        else:
            return {"message" : "key cannot be validated"}, 401

        print(type(key))
        print(key)

        encoded = bytes(key, 'utf-8')
        decoded = encoded.decode('utf-8')
        print(type(decoded))
        print(type(encoded))

        j = config.json.loads(base64.urlsafe_b64decode(decoded))
        print(type(j))

        print(decoded)
        return {"X-API-KEY" : decoded, "message" : "Success"} , 200
    except Exception as e:
        return {"message" : "Error"} , 500

def generate_key(uid, pwd, auth):
    try:
        j = config.json.dumps({"uid": uid, "pwd": pwd, "auth" : auth})
        print(j)
        print(type(j))

        key = base64.urlsafe_b64encode(j.encode('utf-8'))
        print(type(key))
        print(key)

        return str(key)
    except Exception as e:
        return null

def respond_generate_key(uid, pwd, auth):
    key = generate_key(uid, pwd, auth)
    if key != null:
        return key, 201
    else:
        return {"message" : "Key not generated"}, 500