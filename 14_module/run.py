import mod1

print( mod1.add(1, 2) )

# from mod1 import add
# from mod1 import add, sub
from mod1 import *

print( add(1,2) )
print( sub(1,2) )

import sys
print( sys.path ) # 모듈을 가져오는 경로 확인

import folder.calc              # 전체 경로
folder.calc.add()

import folder.calc as fc
fc.add()

from folder import calc         # 파일
calc.add()

from folder.calc import add     # 함수
add()

print('-'*20)
from folder.calc import add as addd
addd()


