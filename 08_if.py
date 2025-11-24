a = 10
b = 5 < a < 20
print(b)

if True :
    print(1)    # 들여쓰기-intent
    print(2)
    if False :
        print(3)
else :
    pass

if a < 5 :
    print(1)
elif a :
 print(2)
else :
  print(3)

if not (a > 3) :
    print(a)

a = True
b = False
if a and b :
    print('and')
elif a or b :
    print('or')

c = False
if not c :
    print('false')

if 1 != 0 :
    print('같지 않다')

money = 2000
# 만약에 money가 
#   3000 이상이면 "택시타자" 출력
#   그렇지 않으면 "걸어가자" 출력
if money >= 3000 :
    print('택시타자')
else :
    print('걸어가자')

card = False
# 만약에 돈이 
#   3000원 이상이거나 카드가 있다면 "택시타자" 출력
#   그렇지 않으면 "걸어가자" 출력
if money >= 3000 or card :
    print('택시타자')
else :
    print('걸어가자')

# 24일에 출석한 학생 명부
student_24 = ['상명', '민서', '우영', '용군', '덕인']
# 24일에 '동현'이 있다면 '복습'출력
# 없다면 '진도나감' 출력
if '동현' in student_24 :
    print('복습')
else :
    print('진도나감')

money = -100
if money < 0 :
    money = 0

if money < 0 : money = 0

# score = input()
# print('>>>', score)

score = input('점수를 입력하세요:')
print('>>>', score, type(score))
score = int(score)

# 점수에 따라
# 90 이상이면 'A'
# 80 이상, 90 미만이면 'B'
# 70 이상, 80 미만이면 'C'
# 그 외 'F' 출력
if 90 <= score :
    print('A')
elif 80 <= score and score < 90 :
    print('B')
elif 70 <= score < 80 :
    print('C')
else :
    print('F')


if 90 <= score :
    print('A')
else :
    if 80 <= score and score < 90 :
        print('B')
    else :
        if 70 <= score < 80 :
            print('C')
        else :
            print('F')

if 90 <= score :
    print('A')
elif 80 <= score :
    print('B')
elif 70 <= score :
    print('C')
else :
    print('F')


# else if와 if의 차이
if 90 <= score :
    print('A')
if 80 <= score :
    print('B')
if 70 <= score :
    print('C')
else :
    print('F')


# else가 있다는건 하나 이상은 꼭 실행된다
if 60 <= score :
    result = '합격'
else :
    result = '불합격'
print(result)

# 위 코드는 아래와 같이 많이 쓴다
result = '불합격'
if 60 <= score :
    result = '합격'
print(result)


result = '합격' if score >= 60 else '불합격'


# student_24 = ['상명', '민서', '우영', '용군', '덕인']
# # 24일에 '동현'이 있다면 '복습'출력
# # 없다면 '진도나감' 출력
# if '동현' in student_24 :
#     print('복습')
# else :
#     print('진도나감')
result = '복습' if '동현' in student_24 else '진도나감'
print(result)

# 조건부 표현식일 때 if와 else는 필수
# result = 123 if 10 < 20
# elif 사용 못함
# result = 123 if 10 < 20 elif 10 == 20 else 5
# print(result)

'''
if 90 <= score :
    print('A')
else :
    if 80 <= score and score < 90 :
        print('B')
    else :
        if 70 <= score < 80 :
            print('C')
        else :
            print('F')
'''
result = 'A' if 90 <= score else 'B' if 80 <= score and score < 90 else 'C' if 70 <= score < 80 else 'F'
result = (
    'A' if 90 <= score else 
    'B' if 80 <= score and score < 90 else 
    'C' if 70 <= score < 80 else 
    'F'
)
print(result)

# 입력 받은 월에 해당하는 계절 출력하기
# 단, 1~12까지만 허용
month = input('월을 입력하세요 : ')
month = int(month)
if 3 <= month <= 5 :
    print('봄')
elif 6 <= month <= 8 :
    print('여름')
elif 9 <= month <= 11 :
    print('가을')
elif 12 == month or 1 <= month <= 2 :
    print('겨울')
else :
    print('1~12까지만 입력하세요')

# 입력 받은 값이 '홀수'인지 '짝수'인지 출력
# 단 조건부 표현식 사용
num = input('숫자 입력 : ')
num = int(num)
result = '홀수' if num % 2 != 0 else '짝수'
print(result)

# 가위바위보 게임 만들기
# '가위' '바위' '보' 입력
# 컴퓨터는 항상 '바위'만 낸다
# '졌다', '비겼다', '이겼다' 출력
game = input('"가위", "바위", "보" 중에서 고르시오 : ')
result = '이김' if game == '보' else '비김' if game == '바위' else '짐' if game == '가위' else '다시 입력해주세요'
print(result)

# a, b 중에 큰 값 출력하기
# 같은 경우 '같다' 출력
a = input('첫번째 숫자 : ')
b = input('두번째 숫자 : ')
result = a if a > b else b if b > a else '같다'
print(result)


game = input('"가위", "바위", "보" 중에서 고르시오 : ')
if game == '가위'
    pass
elif game == '바위'
    pass
elif game == '보'
    pass
else
    print('다시 입력')

match game :
    case '가위' :
        print('짐')
    case '바위' :
        print('비김')
    case '보' :
        print('이김')
    else :
        print('다시 입력')