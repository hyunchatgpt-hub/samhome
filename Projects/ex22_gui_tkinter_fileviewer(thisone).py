# #@@@@ ex2 2교시 시작

# # tikinter file choice & viewer [엑셀 파일을 읽어서..내용을 보여주는 GUI]

# # 기능요구
# #1. 파일선택 버튼을 누르면 엑셀파일을 선택할 수 있어야 함.
# #2. 선택한 파일경로는 Entry 요소에 보여줘야 함.
# #3. '파일읽기'버튼을 누르면 해당경로의 엑셀파일을 pandas 로 읽어야 함.
# #4. '그래프보기'버튼을 누르면 숫자데이터들이 선 그래프로 보여야 함.
# #5. '엑셀데이터보기'버튼을 누르면 다시 표형태의 데이터가 보여야 함.
# #---------------------

# #0. 필요한 라이브러리 추가
# from tkinter import *
# from tkinter import filedialog, messagebox, ttk
# import os #file 경로를 제어하는 표준 모듈
# import pandas as pd # 엑셀처럼 표 형태의 데이터를 쉽게 분석할 수 있는 기능을 가진 외부모듈

# # pandas로 읽은 데이터는 표형태 모습이며. 이를 DataFrame 이라는 타입으로 관리함.
# # 이 파이썬 파일 어디서든 인식하도록.. 전역변수로 선언(만들기)
# data= None #아직은 읽어드리기 전이니까. 다만 이렇게 써놓으면 어디서든 인식이 됨.


# #1. 최상위 컨테이너 위젯 생성
# window= Tk()
# window.title('엑셀 파일 뷰어')
# window.geometry('800x600')

# #2. 파일 선택 영역 Frame
# frame_top= Frame(window)
# frame_top.pack(padx=10, pady=5, fill='x')

# #3. 파일의 경로를 직접입력하거나.. 선택된 파일의 경로가 보여지는 한줄입력 위젯을 Frame에 붙이기
# entry= Entry(frame_top, width=60) #대문자 60글자 정보 들어갈 사이즈
# entry.pack(side='left', padx=5)

# #6. 버튼 클릭시 발동할 함수들 만들기(정의하기)
# #6-1. 파일선택 버튼 클릭시
# def clicked_file_chooser():
#     #7. 파일선택기가 보여지도록 tkinter 의 서브모듈 filedialog 를 import
#     file_path= filedialog.askopenfilename(title='엑셀 파일 선택기', filetypes=[("엑셀 파일들","*.xlsx *.xls"),("모든 파일","*.*")])
#     #선택된 파일경로를 entry요소에 쓰기[단, 선택 안했을 수도 있으니..]
#     if file_path: #파이썬은 None, '', 0 을 제외하고는 모두 참(True)
#         #기존에 선택된 경로가 있다면 지우기...
#         entry.delete(0, END) # 0번 위치부터 끝까지 지우기..
#         entry.insert(0, file_path) #0번 위치부터 글씨 쓰기..
# #----------------

# #6-2. 파일읽기 버튼 클릭시 #@@3교시 시작
# def clicked_file_reader():
#     #엑셀파일을 pandas라는 외부모듈을 이용하여 읽어오기 [필요한 모듈들 추가]
#     #읽어온 데이터를 표형태로 관리하는 DataFrame 객체에 저장
#     #전역변수인 data변수를 사용하겠다고 명시
#     global data

#     #사용자가 선택한 엑셀파일 경로를 읽어오기
#     file_path= entry.get() #Entry 요소에 써있는 글씨 취득..
#     if not os.path.exists(file_path): #경로에 파일이 없다면?
#         #사용자에게 안내문구(메세지박스)를 보여주고.. 파일 읽기 기능을 더이상 수행하지 않기!
#         messagebox.showerror('파일읽기 오류', '파일을 찾을 수 없습니다.')
#         return # 함수 종료...
    
#     data = pd.read_excel(file_path)
#     #일단, 잘 읽어지는지 확인차.. console 창에 출력해보기
#     print(data)

#     #읽은 표형태의 데이터를 GUI로 보여주는 코드 작성.. 이게 너무 길것같아서..
#     #별도의 함수 영역을 만들어서 호출
#     show_data()


# #4. 파일선택 버튼 [ Entry 요소 옆에 ]
# btn_file_chooser= Button(frame_top, text='파일선택', command=clicked_file_chooser)
# btn_file_chooser.pack(side='left', padx=5)

# #5. 선택된 파일 읽기 버튼 [ 파일선택 버튼 옆에 ]
# btn_file_reader= Button(frame_top, text='파일읽기', command=clicked_file_reader)
# btn_file_reader.pack(side='left', padx=5)



# #[파일읽기] 버튼 클릭시 읽어온 data를 GUI로 보여주는 코드가 작성된 함수영역
# def show_data():
#     #전역변수인 표형태의 데이터를 사용하겠다고 명시
#     global data
#     #보여줄 데이터가 없으면 하지마!!
#     if data is None: 
#         return #리턴을 하면 쇼 데이터의 기능은 사실상 끝남
    
#     #기존 표 모양이 있다면 모두 제거!!
#     treeview.delete(*treeview.get_children()) #*(언패킹 연산자) 리스트나 튜플 안의 요소를 개별 인자로 풀어주는 기능 함수명[10,20,30] --> 함수명(10,20,30)

#     #새로운 표 모양 만들기
#     #표의 칸(column)들의 이름을 treeview가 알아야 함
#     treeview['columns']= list(data.columns) #컬룸명들... 컬룸에는 칸이 이만큼있어라고, 칸을 설정하는것임
#     treeview['show']='headings' #이걸 지정하지 않으면 컬룸명이 표시되지 않음

#     #표의 제목줄(heading)에 컬룸명들 설정해주기..
#     for col in data.columns:
#         treeview.heading(col, text=col) #보여질 글씨
#         treeview.column(col, width=120) # 칸 너비

#     #데이터 삽입
#     for idx, row in data.iterrows(): #데이터프레임의 각 줄을 이터레이터로 반복 접근
#         print(list(row))
#         treeview.insert("", "end", vlaues=list(row))
#         #"":최상위 레벨(parent -- treeview)
#         #"end" : 마지막 줄에 추가
    
#     #그래프 형태로 Treeview 에 데이터를 표시하는 기능 함수
#     def show_graph():
#         global data
#         if data is None:
#             return
        
#         #기존 표 구조들을 모두 제거
#         treeview.delete(*treeview.get_children())

# #@@@@ ex2 2교시 끝

# #7. GUI의 나머지 영역 요소들 배치하기
# # 구분선 요소와 표를 보여주는 Treeview 요소는 tkinter의 하위 모듈 ttk 안에 있음.. import
# seprator= ttk.Separator(window, orient='horizontal') #수평선
# seprator.pack(pady = 10, fill='x')

# #버튼 2개를 배치하기 위한 Frame 설치
# frame_bottons=Frame(window)
# frame_bottons.pack(anchor = 'center')

# #버튼 2개를 위 프레임에 붙이기

# btn_show_data = Button(frame_bottons, text='엑셀데이터 보기', command=show_data)
# btn_show_data.pack(side='left', padx=10)

# btn_show_graph = Button(frame_bottons, text='그래프 보기', command=show_graph)
# btn_show_graph.pack(side='left', padx=10)

# #그래프 또는 표 형태로 위젯들을 보여주는 Treeview를 나머지 영역모두 차지하도록 배치
# treeview= ttk.Treeview(window)
# treeview.pack(expand=True, fill='both', padx=10, pady=10)
# #expand=True, fill='both'를 조합하면 화면을 꽉 채우는 효과

# #---------------------------------
# # 윈도우 보여주고 사용자 이벤트 감지하기..
# window.mainloop()
