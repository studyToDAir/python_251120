class FourCal :

    # 생성자
    # 생성할 때 무조건 실행되는 함수
    # 전달인자가 안 맞으면 생성이 안된다
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def setData(self, x, y) :
        self.x = x
        self.y = y

    def add(self) :
        return self.x + self.y

# 뭐.뭐(FourCal)

a = FourCal(1,2)
print( type(a) )

b = FourCal(30, 45)
print( id(a), id(b) )

a.setData(3,4)
print('a.x :', a.x)

b.setData(30,40)
print('b.x :', b.x)

print( 'a.add()', a.add() )
print( 'b.add()', b.add() )

# c = FourCal()
# c.add()

class FourCal2 :
    STATIC_VAR = '생성 없이 사용 가능'

    def __init__(self) :
        self.x = 5
        self.y = 10
    def add(self) :
        return self.x + self.y

class MoreCal2 ( FourCal2, FourCal ) :
    def pow(self) :
        return self.x ** self.y
    def add(self) :
        return self.x + self.y + 1

d = MoreCal2()
print( 'd.x : ', d.x )
print( 'd.add()', d.add() )
print( 'd.pow()', d.pow() )

print( FourCal2.STATIC_VAR )
print( MoreCal2.STATIC_VAR )
print( d.STATIC_VAR )

class Account :
    __a = 10 # 내 클래스 안에서만 사용 가능한 변수 (java의 private)
    def __init__(self) :
        self.__money = 100
    
a = Account(100)
a.__money = 10000
print(a.__money)
print(a.__a)


