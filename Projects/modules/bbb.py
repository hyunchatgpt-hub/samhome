def display():
    print('bbb modules의 display 함수')

#함수 호출문
display()

def output():
    print('output function.........')


    #만약, 어떤 함수를 해당 파이썬 파일에서 실행할때만 호출 되도록 하고 싶다면 
#즉, import 할떄 실행하지 말고.. 이 모듈파일을 직접 실행할떄만 호출되도록 하고 싶다면?
#파이썬에 내장된 특별한 변수 _name_ 를 활용

#__name__변수는 이 파일을 실행하는 주체가 누구인지 확인이 가능함
#이 파일 자체를 실행하면 '__main__'라는 문자열이 출력됨 
#만약, 모듈 import로 실행이 되었다면 그 '모듈명'으로 출력됨
print(__name__)

#output() 함수를 이 파일을 직접 실행할때만 호출하고.. import될때는 안되도록 하려면?
if __name__ == '__main__': #@@혹시 네임와 메인이 같으면 그때만 아웃풋을 호출하라는것임 #@@ 
    output()
