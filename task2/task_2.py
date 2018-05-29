
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


def createUserAPI(user):
    print("=========================================")
    print("=========================================")
    
    print("API calls go here to create user on Intercom")
    print("\n")
    print("user info can be accessed by getters from User class")
    print("\n")
    print("User info : {}, {}, {}".format(user.getId(), user.getName(), user.getEmail() ))

readFromDB()
