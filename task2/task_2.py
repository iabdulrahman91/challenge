
class User(object):
    def __init__(self,userId=0,name='',email=''):
        self.id = userId
        self.name = name
        self.email = email

    def __repr__(self):
        return ("user ID : {} , name : {} , email : {}".format(self.id, self.name, self.email))

    def getId(self):
        return self.id
    def setId(self,userId):
        self.id = userId
        
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
        
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email


# I used pymysql as connector/driver to mysql database
# this require installation, I used pip install 'python3 -m pip install pymysql'
# the database I connect to is on my machine, for testing purpose.

import pymysql

def readFromDB(host='localhost', user='root', password='', db='test'):

    try:
        connection = pymysql.connect(host,user,password,db)
    except:
        print("cannot connect to the database")

    try:
        cursor = connection.cursor()
        cursor.execute('select * from user')
    except:
        print("cursor issue")

    try:
        result = cursor.fetchall()
        for i in result:
            try:
                user = User()
                user.setId(i[0])
                user.setName(i[1])
                user.setEmail(i[2])
                createUserAPI(user)
            except:
                print("user cannot be created")
    except:
        print("cannot fetch")

    connection.close()

# I was not able to implement more at this point since I do not have access to intercom APIs
# I However User class has getters and setters which are helpful in calling the APIs.
# The support of python/Intercom was not provided by Intercom; Third-party lib is needed.
# python3 -m pip install python-intercom.
# https://github.com/intercom/python-intercom

def createUserAPI(user):
    print("=========================================")
    print("=========================================")
    
    print("API calls go here to create user on Intercom")
    print("\n")
    print("user info can be accessed by getters from User class")
    print("\n")
    print("User info : {}, {}, {}".format(user.getId(), user.getName(), user.getEmail() ))

readFromDB()
