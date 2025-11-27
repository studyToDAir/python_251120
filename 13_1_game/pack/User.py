class User :
    def __init__(self, id):
        self.__id = id
        self.__level = 1
        self.__inven = []
    
    def setLevel(self, level) :
        self.__level = level

    def getLevel(self) :
        return self.__level

    def getInven(self) :
        return self.__inven
    
    def addInven(self, item) :
        self.__inven.append(item)
    
    def delInvel(self, item) :
        self.__inven.remove(item)

    
    def printInfo(self) :
        print(f'id : {self.__id}')
        print(f'level : {self.__level}')
        print(f'inven : {self.__inven}')

    def __str__(self) :
        return f'(str)User(id:{self.__id}, level:{self.__level}, inven:{self.__inven})'

    def __repr__(self) :
        return f'(repr)User(id:{self.__id}, level:{self.__level}, inven:{self.__inven})'
    