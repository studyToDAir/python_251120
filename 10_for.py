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
