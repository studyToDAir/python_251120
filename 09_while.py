a = 0
while a < 5 :
    print(a)
    a += 1
print('>>>', a)

# 반복 횟수를 잘 모를때 while
# 반복 횟수를 정확히 알때 for

money = 300
while True :
    print('남은 금액 :', money)
    money -= 100
    if money <= 0 :
        break

count = 10
while count > 0 :
    count -= 1
    # if count % 3 != 0 :   # 3의 배수가 아닐 때
    #     print(count)
    if count % 3 == 0 : # 3의 배수일 때
        continue
    print(count)

count = 0
while count < 5 :
    count += 1
    # if count == 20 :
    if count == 2 :
        break
    print( f'count : {count}' )
else :  # while이 조건에 의해 종료 될 때 실행
        # 즉, break를 안만나면 else가 실행된다
    print('break 안만남')

# while ~ else 이해를 높여보자
# 0~9 사이에 7이 있는지를 찾아보자
n = 7   # 찾을 값
i1 = 0
i2 = 9
isFound = False
while i1 < i2 :
    if i1 == n :
        print('찾음')
        isFound = True
        break
    i1 += 1
if not isFound :
    print('못찾음') 
    
while i1 < i2 :
    if i1 == n :
        print('찾음')
        break
    i1 += 1
else :
    print('못찾음')



# do while 없음
"""
do {
    menu = input('''
    1: 아아
    2: 라떼
    3: 종료
    ''')
    print (주문 처리)

} while (menu != 3);
"""




