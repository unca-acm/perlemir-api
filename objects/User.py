"""
  Author:     Lane Adair (ladair@unca.edu)
  Date:       February 4, 2020
  Version:    0.0.1

  This class sets up for a user object. There can be no user without a user id.
"""



#v0.0.1
class User:
    #This is the constructor
    def __init__(self, fName, lName):
        self.setFName(fName)
        self.setLName(lName)

    def setFName(self, fName):
        self.fName = fName

    def setLName(self, lName):
        self.lName = lName

    def setEmail(self, email):
        self.email = email

    def setUsername(self, username):
        self.username = username

    # def getLastLogin():

u = User('Lane', 'Adair')

print(u.fName)