import time

def delay() :
    time.sleep(1)
    print('2초 뒤')

print('시작')
for i in range(3) :
    delay()
print('끝')

import threading
print('스레드 시작')

for i in range(3) :
    t = threading.Thread(target=delay)
    t.start()

print('스레드 끝')

def delay2(x) :
    time.sleep(1)
    print(x, '1초 뒤')

for i in range(3) :
    t = threading.Thread(target=delay2, args=(str(i)))
    t.start()

