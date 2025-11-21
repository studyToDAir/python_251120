a = ''
print( type(a) )
print( 1, a.strip() )

a = []
a = list()
print( type(a) )
# print( 2, a.strip() )

a = [1,2, 3]
print(a)
print(a[-1])

print(a[0:2])

b = 'abcde'
print( b[1:4] )

print( a[:2] )
print( a[1:] )
print( a[1:100] )

c = [1,2,3,4,5,6,7,8,9]
print( c[5:2] )

# c[0:2] = 2
print( c[:] )

a = a + c
a += c

a = a * 3
a *= 3

# a -= 3

a = [1,2,2,2]
del a[1]
print(a)

b = [1,2,3,4,5]
del b[1:3]
print(b)

c = [1,2,3]
c.append(40)    # 마지막에 추가
print(c)
c.append([100, 200])
print(c)

d = [78,3,4,6,31]
d.sort()
print(d)

d.reverse()
print(d)


list1 = d.sort()
print(list1) # None

e = [1,2,3,4,3]
print( e.index(3) )
# print( e.index(30) )
# print( e.find(3) )
print( 3 in e )

e.insert(2, 50)
print( e )

f = [1,2,3,4,3]
f.remove(3) # 왼쪽부터 해당 값 하나만 삭제
# f.remove(50) # 없으면 에러
print(f)

g = [1,2,3,4]
h = g.pop() # 마지막 것을 빼서 돌려줌
print(h, g)

i = [1,2,3,3]
j = i.count(3)
print( j )

i.extend([10,20])
print(i)
i += [100,200]
print(i)

# i.sort().reverse()
