test_list = ['a', 'b', 'c']
for letter in test_list :
    print(letter)

for letter in 'hello' :
    print(letter)
print(letter)

d = {
    'a': 'aa',
    'b': 'bb',
    'c': 'cc',
}
# 딕셔너리는 key로 반복 가능
for key in d :
    print(key, d[key])

d.keys()
d.values()
d.items()
# for (k, v) in d.items()
for k, v in d.items() :
    # print('k :', k, ', v :', v)
    print(f'k : {k}, v : {v}')

r = range(5)
print('range(5) :', r)
r = range(0, 5)
print('range(0, 5) :', r)
print( list(r) )
# range (시작숫자, 종료숫자+1, 건너뛰기)

for i in range(0, 5) :
    print(i)

print('-' * 20)
for i in range(2, 5) :
    print(i)

print('-' * 20)
for i in range(2, 10, 3) :
    print(i)

print('-' * 20)
for i in range(10, 2) :
    print(i)

print('-' * 20)
for i in range(10, 2, -1) :
    print(i)

print('=' * 20)
# 1부터 100까지 모두 더한 값 출력 : 5050
result = 0
for i in range(1, 100+1) :
    result += i
print(result)

# 1~100까지 3또는 5의 배수는 제외하고 모두 더하기
print('=' * 20)
result = 0
for i in range(1, 100+1) :
    if (i % 3 == 0) or (i%5 == 0):
        continue
    result += i
print(result)

print('=' * 20)
arr = [51,52,53,54,55]
idx = 0
for value in arr :
    print(idx, value)
    idx += 1

print('=' * 20)
for i in range( len(arr) ) :
    print(i, arr[i])

for i in range(5):
    print(i, end=',')

## 구구단 출력
# 2단
'''
2x1=2
2x2=4
'''
for i in range(1, 10) :
    print(f'2x{i}={i*2}')

for i in range(1, 10) :
    print(f'3x{i}={i*3}')


for j in range(2, 10) :
    print(f'--{j}단--')
    for i in range(1, 10) :
        print(f'{j}x{i}={i*j}', end='\t')
    print()


for i in range(5) :
    print(i)
else :
    print('break 안만남')

for i in range(5) :
    print(i)
    break
else :
    print('break 안만남')


print('#'*20)
#####################
# 리스트 컴프리헨션 comprehension

for i in range(1, 10) :
    print(i)


a4 = '''
    *
   ***
  *****
 *******
'''
a5 = '''
    *
   ***
  *****
 *******
*********
'''
print(a5)

# 1,2,...,9 값을 가지는 리스트를 쉽게 만들어보자 
a = [1,2,3]
'''
    리스트 선언 a
    반복 1~9 만큼
        a에 하나씩 추가
    a 출력해서 확인
'''
a = []
for i in range(1, 10) :
    a.append(i)
print(a)

print('-'*20)
a = [ i for i in range(1, 10)  ]
print(a)

# 17의 배수 5개
b = []
for i in range(1, 6) :
    b.append(17 * i)

b = [ (i * 17) for i in range(1, 6)  ]

for i in range(17, (17*5)+1, 17) :
    b.append(i)
b = [ i for i in range(17, (17*5)+1, 17) ]

c = []
for i in range(1, 10) :
    if i % 3 == 0 :
        c.append(i)

for i in range(3, 10, 3) :
    c.append(i)

c = [i for i in range(1, 10) if i % 3 == 0 ]
print(c)

c = []
for i in range(1, 10) :
    if (i % 3 == 0) or (i % 5 == 0):
        c.append(i)
c = [ i for i in range(1, 10) if (i % 3 == 0) or (i % 5 == 0) ] 

# 1~9까지에서
# 홀수는 그대로
# 짝수는 2배 인 배열을 만들자
for i in range(1, 10) :
    # 1단계
    if i % 2 == 0 :
        c.append(i * 2)
    else :
        c.append(i)

    # 2단계
    if i % 2 == 0 :
        value = i * 2
    else :
        value = i

    # 3단계
    value = i*2 if i % 2 == 0 else i
    c.append(value)

    # 4단계
    c.append(i*2 if i % 2 == 0 else i)

        
c = [ i*2 if i % 2 == 0 else i for i in range(1, 10) ]

print('-'*20)
## 구구단
d = []
for i in range(2, 10) :     # 바깥쪽
    for j in range(1, 10) : # 안쪽
        d.append(f'{i}x{j}={i*j}')
print(d)

# 안쪽부터
e = [ [ f'{i}x{j}={i*j}' for j in range(1, 10) ] for i in range(2, 10) ]
# 이건 의도와 다르게 2차원 배열이 된다
print('--- e ---')
print(e)

# 그렇다면
f = [f'{i}x{j}={i*j}' for i in range(2, 10) 
                      for j in range(1, 10)]
print('--- f ---')
print(f)

# 딕셔너리 컴프리헨션
a = {
    '0': 0,
    '1': 1,
    '2': 4,
    '3': 9,
    '4': 16
}
a = {}
for i in range(5) :
    if i%2 == 0 :
        a[i] = i ** 2

a = {  i : i**2 for i in range(5) if i%2 == 0 }
print(a)

print('-'*20)
a = [11,12,13,14]
for i, data in enumerate(a) :
    print(i, data)
print('-'*20)
for i, data in enumerate(a, 2) :
    print(i, data)

print('-'*20)
a = [10,20,30]
b = [6,7,8,9]
c = zip(a, b)
print(c)
d = list(zip(a, b))
print(d)

lang = 'Kor'
kr = ['소개', '채용']
en = ['About', 'Recruit']

# '소개'를 출력
if lang == 'Kor' :
    print(kr[0])
elif lang == 'Eng' :
    print(en[0])

i18n = []
if lang == 'Kor' :
    i18n = kr
elif lang == 'Eng' :
    i18n = en

html = f'''
    <span>{i18n[0]}</span> <span>{i18n[1]}</span>
'''

d_kr = {
    'common.header.about' : '소개'
}

d_en = {
    'common.header.about' : 'About'
}

# if를 통해서
i18n = d_kr

html = f'''
    <span>{i18n['common.header.about']}</span>
'''


'''
문제1
1~n 까지 짝수의 합을 구하기

문제2
1~n 까지 숫자를 3개씩 옆으로 찍기

문제3
+++*---
++***--
+*****-
*******

문제4
주사위 2개를 굴려서 중복을 제거한 경우의 수
[1, 2] [2, 1] : 중복이라서 하나로 보기

문제5
키오스크 처럼 
'1: 아아, 2: 라떼, x: 종료'
'1' 입력 시 "아아" 출력
'x'가 입력되기 전까지 무한 반복
'''
# 1~n 까지 짝수의 합을 구하기
n = 10
result = 0
for i in range(1, n+1) :
    if i%2 == 0 :
        result += i
print(result)

'''
문제2
1~n 까지 숫자를 3개씩 옆으로 찍기

1단계 : 1 2 3 4 5 6
2단계 : 3번째마다 엔터
'''
for i in range(1, n+1) :
    print(str(i)+' ', end='')
    
    if i%3 == 0 :
        print()

'''
문제3
+++*---
++***--
+*****-
*******


+++ * ---
++ *** --

4줄
+3(4-1) *1(1*2-1) -3(4-1)      : 1번째 줄
+2(4-2) *3(2*2-1) -2(4-2)      : 2번째 줄
        *5(3*2-1)              : 3번째 줄
'''
print('-'*20)
n = 7
for i in range(1, n+1) :
    # print(i)
    print('+'*(n-i), end='')
    print('*'*(i*2-1), end='')
    print('-'*(n-i), end='')
    print()

'''
문제4
주사위 2개를 굴려서 중복을 제거한 경우의 수
[1, 2] [2, 1] : 중복이라서 하나로 보기
'''
for i in range(1, 6+1) :
    for j in range(i, 6+1) :
        print(f'[{i},{j}]', end=' ')
    print()

