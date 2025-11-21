a = {}
a = dict()
print( type(a) )

b = {
    '이름': '최민수',
    '주소': '천안',
    '오늘': 21,
    '스킬': {
        'java': '상',
        'python': '하'
    }
}
print( b )
print( b['이름'] )
# print( b.이름 )

# print(b['나이']) # key가 없으면 에러

b['나이'] = 20
print( b )

c = { 
    1: '일',
    2: '이'
}
print(c[1])

del c[1]
print( c )

d = {
    '이름': '민수',
    '이름': '최민수'
}
print( d )

e = b.keys()
print( e )
print( type(e) )

print( b.values() )

print( b.items() ) # key, value 튜플로 나옴

d.clear()
print( d )
d = {}

print(b.get('이름'))
print(b['이름'])
print(b.get('이름2')) # key가 없을 때 None을 돌려주며 에러 없음

print( b.get('이름', '값없음') )
print( b.get('이름2', '값없음') )

print( '이름' in b ) # in은 key가 있는지 여부를 판단

e = b.pop('이름')
print( e, b )