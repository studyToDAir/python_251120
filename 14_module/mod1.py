def add(x, y) :
    print('mod1의 add 실행')
    return x + y

def sub(x, y) :
    print('mod1의 sub 실행')
    return x - y

def test() :
    print('test 실행')
    print( add(1, 2) )

# test()

print( '__name__ : ', __name__)
if __name__ ==  '__main__' :
    test()
