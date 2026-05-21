# #tkinter file choice & viewer [엑셀 파일을 읽어서.. 내용을 보여주는 GUI]

# #기능요수
# #1. 파일선택 버튼을 누르면 엑셀파일을 선택할 수 있어야 함.
# #2. 선택한 파일 경로는 Entry 요소에 보여줘야 함.
# #3. '파일읽기'버튼을 누르면 해당경로의 엑셀 파일을 pandas로 읽어야 함.
# #4. 그래프보기 버튼을 누르면 숫자 데이터들이 선 그래프로 보여야 함.
# #5. '엑셀 데이터보기'버튼을 누르면 다시 표형태의 데이터가 보여야 함.

# #AI프롬프트 방식은 이렇게 써야하는것임. 나중에 할 예정. 지금은 레거시 방법으로 진행.
# #----------------------------

# #0. 필요한 라이브러리 추가
# from tkinter import *
# from tkinter import filedialog
# # #1. 최상위 컨테이너 위젯 생성
# # window = Tk()
# # window.title('엑셀 파일 뷰어')
# # window.geometry('800x600')

# # #-------------------------------------
# # # 윈도우 보여주고 사용자 이벤트 감지하기..
# # window.mainloop()

# # #2. 파일 선택 영역 Frame
# # frame_top= Frame(window)
# # frame_top.pack(padx=10, pady=5, fill='x')

# # #3. 파일의 경로를 직접입력하거나.. 선택된 파일의 경로가 보여지는 한줄입력 위젯을 Frame에 붙이기
# # entry= Entry(frame_top, width=60) #대문자 60글자 정보 들어갈 사이즈
# # entry.pack(side='left', padx=5) #엔트리를, 어디다가? 팩 붙일거야, 그리고 프래임을 붙일거야 라는말임

# #1. 최상위 컨테이너 위젯 생성
# window= Tk()
# window.title('엑셀 파일 뷰어')
# window.geometry('800x600')

# #2. 파일 선택 영역 Frame
# frame_top= Frame(window)
# frame_top.pack(padx=10, pady=5, fill='x')

# #3. 파일의 경로를 직접입력하거나.. 선택된 파일의 경로가 보여지는 한줄입력 위젯을 Frame에 붙이기
# entry= Entry(frame_top, width=60) #대문자 60글자 정보 들어갈 사이즈
# entry.pack(side='left', padx=5) #엔트리를, 어디다가? 팩 붙일거야, 그리고 프래임을 붙일거야 라는말임

# #6. 버튼 클릭시 발동할 함수들 만들기(정의하기)
# #6-1. 파일선택 버튼 클릭시
# def clicked_file_chooser():
#     #7. 파일선택기가 보여지도록 tkinter 의 서브모듈 filedialog 를 import
#     file_path= filedialog.askopenfilename(title='엑셀 파일 선택기', filetypes=[("엑셀 파일들","*.xlsx *.xls"),("모든 파일","*.*")])
#     #요 기능의 리턴값이 선택값file_path 이다.
#     #선택된 파일경로를 entry요소에 쓰기[단, 선택안했을 수도 있으니..]
#     if file_path: #파이썬은 None, '', 0을 제외하고는 모두 참(True)
#         #기존에 선택된 경로가 있다면 지우기...
#         entry.delete(0, END)# 0번 위치부터 끝까지 지우기..
#         entry.insert(0, file_path) #0번 위치부터 글씨 쓰기..
# #------------------------

# #6-2. 파일읽기 버튼 클릭시
# def clicked_file_reader():
#     pass

# #4. 파일선택 버튼 [ Entry 요소 옆에 ]
# btn_file_chooser= Button(frame_top, text='파일선택', command=clicked_file_chooser)
# btn_file_chooser.pack(side='left', padx=5)

# #5. 선택된 파일 읽기 버튼 [ 파일선택 버튼 옆에 ]
# btn_file_reader= Button(frame_top, text='파일읽기', command=clicked_file_reader)
# btn_file_reader.pack(side='left', padx=5)


# #---------------------------------
# # 윈도우 보여주고 사용자 이벤트 감지하기..
# window.mainloop()