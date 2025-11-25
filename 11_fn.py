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


##########################
# 내일 이야기 하기로 ...
print('-'*20)
a = 1
def test2(z) :
    a = z+1
test2(a)
print(a)

b = [1,2,3,4]
def test3(z) :
    z.append(5)
test3(b)
print(b)

c = [1,2,3,4]
def test4(c) :
    c = [1,2,3,4,5]
z = test4(c)
print(c)
print(z)
