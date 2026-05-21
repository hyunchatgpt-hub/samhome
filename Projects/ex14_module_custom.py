#나만의 모듈 만들기

#1 별도의 파일(module_a.py)에 함수와 변수를 만들어 사용해보기


#print(title) #error
# show() #error

#다른 모듈(파이썬 파일) 의 변수와 함수를 사용하려면.. import

import module_a
print (module_a.title)
module_a.show()

# 모듈명 없이 변수와 함수명을 사용하려면..
from module_a import title, show
print(title)
show()

#특정 모듈의 모든 변수와 함수를 쉽게 사용하고 싶다면..
from module_a import *
print(title)
show()
print()
#------------------------

import modules.aaa
print(modules.aaa.title) #@@폴더안에 aaa안에 파일이 있고, 그 안에 타이틀이라는 변수가 있다 라는 느낌임.
modules.aaa.show()
print()

from modules import aaa #@@ (모듈 폴더안에있는 aaa 파일만 가지고 오겠다)
print(aaa.title)
aaa.show()
print()
#------------------------------------------

#모듈을 import 한다는 것은 사실.. 그 파이썬파일.py를 실행한다는 것임
from modules import bbb #@@ 이 폴더로부터 임포트 하자. bbb만. if __name__ == '__main__': 이거에 대해서 복습 필수.

#bbb모듈의 output()함수를 호출하고싶다면..
bbb.output() #@@안에 아웃풋을 호출하면 됨
print()
#---------------------

#_(언더스코어)를 변수명에 사용하면 import * 로 가져올때 제외됨..
from modules import ccc #@@모듈스 라는 폴더에서 임포트 해올게요, 누구를?씨씨씨를
print(ccc.title)
print(ccc._message_a) #이때까지는 문제없이 나옴.

from modules.ccc import *
print(title)
# print(_message) #여기서 못알아듣게됨. 인식안됨 즉 임포트로 모든거 할떄 제외하고 싶다는게 언더스코어임. 
#import * 일떄만 제외되는 것이어서.. 직접 대상을 명시하며 import 하면 사용이 가능.

from modules.ccc import _message_a
print(_message_a) 

#@@왜 이렇게 만들었을까? 별을 만들면 모든 변수 함수등을 다 가지고 가니까, 언더바 하나만 써서 제외시키는걸 만든것임.