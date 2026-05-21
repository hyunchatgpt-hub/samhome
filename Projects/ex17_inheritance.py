#상속 - inheritance -- 이미 설계된 다른 클래스를 상속받아 새로운 멤버만 추가하는 문법

#문법보다는.. 대략적으로 상속을 받는 다는 것을 알아보는 예제

#1. 게임 캐릭터 종류: Robot, FlyRobot, SwimmingRobot
# Robot        : 이동기능, 공격기능
# FlyRobot     : 이동기능, 공격기능, 나는 기능
# SwimmingRobot: 이동기능, 공격기능, 수영기능

#캐릭터마다 보유한 기능이 다르기에 각각 class 설계도를 만들어야 함.
class Robot:
    #이동 기능
    def move(Self):
        print('아장아장..')

    #공격 기능
    def attack(self):
        print('주먹발사!!')

#@@위에는 설계도 면뿐이다. 그래서 객체를 생성해야함
#로봇 객체 생성
r = Robot() #@@ 이건 생성자 함수이다.
r.move() #@@ 알 기능을 쓰려면. 점 을 하면 접근 연산자이다.
r.attack() #@@ 이동해, 그리고 공격해 라는것이다.
print()

#공중유닛 (하나만 만드니 재미없어서 하나 더 만들기)
class FlyRobot(Robot):
    #로봇이라면 가져야할 기본기능(이동, 공격)을 다시 작성하려니.. 짜증
    #저 위 Robot class 설계도면에 이미 이동과 공격기능이 있으니..
    #이를 상속받아 새로운 기능만 추가하면 더 빠르게 설계가 가능..
    #dnl class FlyrRobot: <-- 여기 옆에다가 괄호 로봇을 쓰면 로봇 기능을 상속받는것이다.

    #새로운 기능(나는 기능)
    def fly(self):
        print('오~~~ 나다')

#공중유닛 로볼 객체를 생성해보기.
fr = FlyRobot() #<--- 객체 생성하는 방법.
fr.move() #역기서 점찍고 미리보기 보면 거기 기능들이 나와있다
fr.attack()
fr.fly()
print()

#해상유닛 [Robot + 수영기능]
class SwimmingRobot(Robot):
    #이미 move4(), attack() 보유한 상태
    def swimming(self):
        print('음~파! 음~파!')

sr = SwimmingRobot()
sr.move()
sr.attack()
sr.swimming()
print('-'*30)
print()
#---------------------------------------------------------------------

#2. 상속 문법에 대해 조금 더 알아보기
# First 클래스 <- Second 클래스 <- Third 클래스 @@퍼스트 클래스가 있고, 이걸 세컨드가 상속받고, 그걸 써드가 상속받는걸 만들어볼것임 (화살표는 parents 부모클래스로.)

class First:
    #초기화 함수 (생성자)를 만들어 멤버변수 a 를 만들기
    def __init__(self):
        self.a = 10    #@@셀프에 에이라는 멤버 면수를 만들어라.
        print('First class constructor!')
    
    def show(self): #멤버함수(메소드) 정의
        print('a:', self.a) #@@ 쇼가 호출되면, a라는 멤버변수를 출력한다는 뜻임.
#------------
#@@ 원래는 바로 이거였음 (지움)
#@@ f = First()#@@객체 만드는 방법 이렇게 만들면 자동으로 이니셜 First class constructor!가 발동한. 하지만 쇼는 부르지 않았기떄문에 발동하지 않음
#@@ f.show() #쇼를 발동해야 나옴.
#---------------
#First 클래스를 상속하는 Second 클래스 설계해보기
class Second(First): #이렇게 퍼스트 클래스를 상속
    #pass #우선은 패스해서 에러나지 않게해놓음. (나중에 지움)
    #이 클래스도 초기화함수(생성자)를 만들어 새로운 멤버변수를 추가할 수 있음.
    def __init__(self):
        #파이썬언어에서는 자식클래스의 생성자를 명시적으로 사용할때는
        #반드시 부모클래스의 생성자를 명시적으로 호출해야만 상속이 됨.
        #@@ 이닛을 안하면 자동으로 상속을 해서 에러가 안나는데, 만약 이닛을 하면, 초기화되기때문에 부모 클래스를 상속하겠다고 명시해줘야함
        #상속해주는 클래스를 보통 [부모parents 클래스 or 슈퍼super 클래스] 라고 부름
        #상속 받는 클래스를 보통 [자식child 클래스 or 서브sub 클래스] 라고 부름

        #부모 생성자를 명시적으로 호출하기!!
        super().__init__() #@@ 이렇게 쓰면, 부모를 만들거구나 라고 인식하고 퍼스트와 세컨드가 둘다 출력됨
                           #가급적 부모생성자 호출코드를 첫줄에 작성하는 것을 권장.!
        #본인만의 멤버 추가
        self.b = 20
        print('second class constructor!!')

    #상속받은 First의 show()출력기능 함수의 기능을 재정의 하여 개선... override
    def show(self):
        # print('a:', self.a)
        #a 변수는 First 클래스의 멤버이며.. 이 값을 출력하는 기능은 
        # 이미 First 부모클래스의 show()로 만들어져 있고.. 이를 상속해왔기에.. 
        super().show() #부모의 슈퍼를 부르겠다는 뜻. 부모것은 부모가 출력
        print('b:', self.b) # 내것은 내가 출력

#Second 객체 생성
s = Second() #@@ 세컨드 객체를 만든것임. #@@ 이 상태에서 출력하면, 퍼스트를 가지고 와서, 퍼스트 (First class constructor) 가 출력되는것을 볼 수 있다.
             #상속은 부모클래스의 멤버만 쪽 뽑아오는 것이 아니라.. 자식 객체를 생성할때 그 안에 부모 객체로 생성하여 사용하는 문법(마치. 러시안 인형처럼..)..  Second 객체만 생성해도 First 객체의 생성자 함수가 실행되는 것을 확인할 수 있음.
#s2 객체를 만들어서 s2 = Second() 이렇게 하면...????
#상속을 받으면 부모객체를 멤버를 내것인양 쓸 수 있도록 해주는 것임
print(s.a) #여기 에이는 퍼스트 클래스의 멤버임 #부모의 멤버를 내것인양
print(s.b) # 자식만의 고유 멤버
print()

#멤버 변수의 값을 직접 출력하는 것 짜증..
#멤버 변수의 값을 출력해주는 기능함수를 이용
# 가만보니. 상속받은 First 클래스에 show()라는 출력기능 함수가 존재함.
s.show()
#위 기능은 a변수만 출력해줌...
#즉, 상속받은 기능함수가 있지만.. 그 기능함수의 동작이 맘에 안들 수도 있음.
#상속받은 기능함수가 맘에 들지 않을떄 이를 재정의 하여 기능을 개선하도록 함
#이를 함수의 오버라이드 override 라고 부름 (기존에 것을 놔두고 그 위에 올라타는 개념임. overwrite 처럼 기존것을 없애는게 아님.)
#재정의를 하면... 
s.show() # 재 정의된 second의 show가 발동함.

# Second를 상속하는 Third 클래스 만들어보기..[부모<-자식<-손주]
class Third(Second):
    def __init__(self): #상속받는 걸 쓰면, 슈퍼로 명시적으로 아래 써야한다. 문법임.
        super().__init__()
        print('Thrid class constructor!!')
        self.c = 30
#----------------------
t = Third()
print(t.a, t.b, t.c) #예는 a b c 다 가지고 있음
print("-"*30)
print()
#----------------------------

#[상속 마무리 예제]
#어떤 대학앱의 회원 데이터 저장 [회원종류 여러개]
#일반회원 : 이름, 나이
#학   생 : 이름, 나이, 전공
#교   수 : 이름, 나이, 연구과제
#근로학생 : 이름, 나이, 전공, 업무

#1] 일반회원
class Person:
    def __init__(self, name, age): #@@멤버변수가 있으면 이걸 써줘야함
        self.name = name #@@네임변수 값을 미리 써놓을 수가 없으니, 파라미터로 생성할때 값을 받자라는것임)
        self.age = age
        print('Person 객체 생성')
    
    def show(self): # 이 값을 출력해주는 쇼기능
        print('이름:', self.name)
        print('나이:', self.age)
#----------------- 여기까지가 퍼슨임. 멤버변수2개, 멤버함수 1개

p = Person('sam', 20) #퍼슨 만들어, 이름과 나이가 필요함.
p.show() #피한테 쇼 해달라고 함.
print()

#[2] 퍼스트를 상속받은 학생회원
class Student(Person):
    def __init__(self, name, age, major): #@@이 3가지 정보를 받아야한다고 써주는것임. 이렇게 되면, 부모클래스를 불러라라는것을 해야함
        super().__init__(name, age) #부모를 부를떄 이름과 나이를 전달해라 라는 뜻으로 괄호에 넣어야함. 부모의 멤버는 부모가 초기화
        self.major = major #나만의 멤버면수. 내껀 내가...
        print('Student 객체 생성')

        #상속받은 show는 [이름, 나이]만 출력함. 그래서 기능개선 override 재정의
    def show(self): #그래서 디파인해서 쇼를 다시 만듬
        super().show() #부모의 값들은 부모/슈퍼의 쇼로 대신해라
        print('전공:', self.major) # 내껀 내가 출력

#--------------------------------

stu = Student('robin', 23, 'ai web') #객체생성
stu.show()
print()

#3 교수회원
class Professor(Person):
    def __init__(self, name, age, subject): #이렇게 4개를 받는다는것임
        super().__init__(name,age) #상속받은걸로 네임과 에이지를 처리하고
        self.subject = subject #내껀 내가 만듬
        print('Professor 객체 생성')

    def show(self): #쇼를 오버라이드
        super().show()
        print('연구과제:', self.subject)
#-----------------------------------------------------

pro = Professor('park', 45, 'ai data analysis')
pro.show()
print()

#4] 근로장학생
class AlbaStudent(Student):
    def __init__(self, name, age, major, task): #멤버변수 초기화
        super().__init__(name, age, major) #이건 스튜던트에서 알아서 하세요
        self.task = task #나는 태스크만 관리할게요
        print('AlbaStudent 객체생성')
    
    def show(self):
        super().show() #부모야 니꺼에 쇼기능이 있다면 쇼 출력해
        print('업무', self.task) #내껀 내가할게
#----------------------------------------

alba = AlbaStudent('hong', 25, 'data', 'pc management')
alba.show()
print()

#모든 책의 내용 끝 500페이지 까지 끝남.