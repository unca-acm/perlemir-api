import json
from perlemir_api.config import config
#*********************************************************
#                   USER LOGIN FUNCTIONS
#*********************************************************
def login(uName, pwd):
    #check the username first to see if the user exists
    if checkUID(uName):
        #the following will execute if the user is found
        if checkPWD(uName, pwd):
            print("test")
            return 200
        #end if

        return 503
    else:
        return 404
    #end if
#end login(String, String)

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
        f = open('/Users/laneadair/Desktop/Algo-bot-api/python/ud/users.json')
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
        f = open('/Users/laneadair/Desktop/Algo-bot-api/python/ud/users.json')
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
def logout():
    print("LOGOUT")

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
