# a = add(1, 2)  # 함수 선언 이후에 사용 가능

def add(x, y) :
    z = x + y
    return z
a = add(1, 2)
print(a)

def sub(x, y) :
    return x - y
a = sub(1, 2)
print(a) # -1
b = sub(y = 2, x = 1)
print(b)

# c = sub(1,2,3)
# c = sub(1)
print(1, 2, 3, 4)
# def print(*datas, end='\n', sep=' ') :

def add_many(*a) :
    print(type(a), a)
    for data in a :
        print(data)

add_many(1,2)
add_many()

def menu(pizza, *topping) : # 가변인자는 특성상 가장 마지막에 한번 밖에 못 옴
    print(pizza, topping)

menu('슈프림', '버섯', '옥수수')

def make_dict( **kwargs ) :
    print( type(kwargs), kwargs )

make_dict(x=5)
make_dict(x=5, y=10)
make_dict(key='value')
# make_dict(10) # **로 받을 때는 key = value 형태만 가능
make_dict()

def test_complex( *a, **b) :
    print('a :', a)
    print('b :', b)

test_complex(1,2,3)
test_complex(1,2,3, x=5)
test_complex(x=5)
# test_complex(x=5, 1,2,3)

def test_tuple() :
    # return (1, 2)
    return 1, 2
    # return 1, 2, 3
    return [1, 2]   # 리턴이 여러개라도 에러 안남
a = test_tuple()
print(type(a), a)
b = a[0]
c = a[1]

b, c = test_tuple()
print(type(b), c)

def user_info(name, job, nation='한국') :
# def user_info(name, nation='한국', job) :
    print(name, job, nation)

user_info('a', 'b', 'c')
user_info('a', 'b')

# 같은 이름으로 재선언 하면 덮어 써진다
def add(x, y) :
    z = x + y
    return z + 1

print(type(add))
add(1,2)
z = add(1,2)
print(a)

# add = 1
# add(1,2)
# print = 'abcd'
p = print
p(123)

def test1() :
    t = 1 # 지역변수
test1()
# print(t)

print('='*20)
def test999() :
    a = 1
    b = 2
    print( locals() )
    c = 3
test999()

print(':='*20)
a = 100
def test2(z) :
    # print(1, a) # 변수 처리
                # 먼저 지역 변수를 찾고
                # 없으면 전역 변수를 찾는다
    a = z+1
    print(2, a)
    z = 200
test2(a)
print(a)

print('-'*20)
b = [1,2,3,4]
def test3(z1) :
    z1.append(5)
test3(b)
print(b)

print('+'*20)
c = [1,2,3,4]
def test4(z2) :
    ## z2 == c

    z3 = [1,2,3,4,5]
    z2 = z3

    # z2 = [1,2,3,4,5]
test4(c)
print(c)

# for a in ...
#     print(a) # 지역변수

## 전역 변수를 바꾸는 방법
### 방법 1
a = 1   
def vartest(z) :
    z = z + 1
    return z
a = vartest(a)

print('-'*20)
a = 1
def vartest2() :
    print(a)

    z = a + 1
    print(z)
vartest2()

print('+'*20)
a = 1
def vartest3() :
    a = 3
    # a = a + 3
vartest3()
print(a)

## 전역 변수를 바꾸는 방법
### 방법 2
print('-'*20)
a = 1
b = 2
def vartest4() :
    global a, b # = 을 이용해서 값을 변경할 때 만 global 쓰면 된다 
    a = 3
    b = 30
vartest4()
print(a)
print(b)

# 내일 만들자
# 내용은 아직 못 정함
# TODO : 낼 하자
def test() :
    pass

# FIXME : 누구씨 고쳐줭~

# chaining
a = " abcd  "
b = a.strip()
c = b.replace('b', 'B')
d = c.count('c')

a.strip().replace('b', 'B').count('c')

# 람다 lambda
x = 3
def test_sqr(x) :
    return x ** 2
a = test_sqr(x)
a = lambda x: x**2

# test_sqr( lambda x: x**2 )

def test(x, y) :
    '''
    Docstring for test
    
    :param x: Description
    :param y: Description
    '''
    return x + y
test(1, 2)

def testDebug(x, y) :
    x = x + 3
    print(x)
    y = x + 5
    print(y)

    return y

testDebug(1,2)
