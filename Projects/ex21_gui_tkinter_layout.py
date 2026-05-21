#ex21-1 #took kit interface tkinter 에서 widget 들을 배치하는 3가지 방법
# pack(), grid(), place()

# 0. 파이썬 GUI용 표준모듈 사용 (외부x)
from tkinter import *

#1. 최상위 윈도우 만들기
window = Tk() #툴킷, 창 같은것임
window.title('gui layout')
window.geometry('400x300+100+50') #너비x높이+x좌표+y좌표
window.resizable(False, False,)

#3. 위젯들을 배치하는 3가지 방법 

#1. pack() : 차례대로 놓여지는 방식 (다른 위젯위에 놓여지지 않음)
btn1 = Button(window, text = 'button #1') #버튼객체 생성
btn1.pack(side='left', anchor='n') #n: north

btn2 = Button(window, text='button #2') #2번쨰 버튼을 만든것임
btn2.pack(side='right', fill = 'y')

btn3=Button(window, text='button #3')
btn3.pack(side='top', anchor='e') #앵커는 east로. 다만 2번이 있을경우 

btn4 = Button(window, text='button #4')
btn4.pack(side='bottom', fill='x') #가운데 채울게요 x축을.

#같은 위치에 다른 위젯이 있으면 그 옆, 위 아래 배치됨.

btn5= Button(window, text = 'button #5')
btn5.pack(side='bottom') # 이미 바닥에 뭐가 있으니 그 바로 위에 배치됨

#2. place() : 절대위치 지정.. 좌표로 위치를 지정(겹칠 수 있음.)
btn6 = Button(window, text='button #6', )
btn6.place(x=50, y=50)

btn7 = Button(window, text='button #7', )
btn7.place(x=70, y=70) #2개가 겹치는게 보임.

btn8= Button(window, text='button #8')
btn8.place(x=0, y=275)


#3. grid() : 격자 위치 지정
#Frame 위젯을 활용 -- window 안에 판넬을 만들어주는 위젯(일부 영역을 만들때 사용)
frame = Frame(window, width=300, height=150)
frame.place(x=0, y=150)

b1 = Button(frame, text='1')
b1.grid(row=0, column=0)

b2 = Button(frame, text='2')
b2.grid(row=0, column=1)

b3 = Button(frame, text='3')
b3.grid(row=0, column=2)

b4= Button(frame, text='4')
b4.grid(row=1, column=0, rowspan=2, sticky=W+E+N+S)

b5= Button(frame, text='5')
b5.grid(row=1, column=1)


b6= Button(frame, text='6')
b6.grid(row=1, column=2)


b7= Button(frame, text='7')
b7.grid(row=2, column=1, columnspan=2, sticky=W+E)
#-------------------
#2. 윈도우를 화면에 보여주고 사용자의 이벤트를 감지하도록...

#@@@@ ex2-1끝
window.mainloop()
