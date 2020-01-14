class Database:
    """
    Database is a singleton class to mimick the behaviour of a database
    """

    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.database = {
                "users": {},
                "posts": {},
                "groups": {}
            }
            Database.__instance = self
    
    def add(self, database, key, item):
        try:
            self.database[database][key] = item
            return True
        except:
            return False

    def delete(self, database, key):
        try:
            del self.database[database][key]
            return True
        except:
            return False
        
    def get(self, database, key):
        try:
            return self.database[database][key]
        except:
            return False

    def getAll(self, database):
        try:
            return self.database[database]
        except:
            return False

    def getUser(self, user):
        try:
            return self.database["users"][user]
        except KeyError:
            print("Username not found!")
            return None