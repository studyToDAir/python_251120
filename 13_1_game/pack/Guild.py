class Guild :
    def __init__(self, name) :
        self.__name = name
        self.__users = []
    
    def addUser(self, user) :
        self.__users.append(user)
    def delUser(self, user) :
        self.__users.remove(user)

    def getRanker(self) :
        return max(self.__users, key=lambda x:x.getLevel())
    
    def getBestSales(self) :
        return max(self.__users, key=lambda x:len(x.getInven()))
    
    def getUsers(self) :
        return self.__users
    
