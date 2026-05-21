# image widget

from tkinter import * #모든 모듈들을 다 
window= Tk() #윈도우 상에서 툴킷으로 만들어
#사이즈 지정이 없으면 안에 내용물을 감쌀만큼의 사이즈로 자동 조절됨

# 이미지파일을 불러와서 tkinter에서 사용 [.jpg는 tkinter가 불어오지 못함.]
img= PhotoImage(file='Projects/images/ms19.png').subsample(2) #포토이미지라는 기능임
# 위 이미지를 보여주는 전용 widget은 없음..대신 글씨를 보여주던 액자..Label 이용
label= Label(window, image=img) #레이블, 윈도우에 붙여라는 말임., 그리고 이미지를 보여줄게 라는 말임, 그 이미지는 어디있어? 위에 img) 
label.pack()

# jpg를 보여주고 싶다면... 외부 모듈이 추가로 필요함
# 파이썬의 이미지작업에 특화된 라이브러리 pillow (python image library)
# 외부모듈을 설치필요 ( pip )
# pip install pillow

# 사용
from PIL import Image, ImageTk #tkinter에서 pillow의 이미지를 인식하도록..

#@@@@ 아래 내용 요약: 파이썬을 열어, 크니까 사이즈 조절해, 그걸 가지고 와서 티킨터용으로 만들어, 티킨터 이미지를 액자에 넣어 그리고 뽑아, 라는 뜻임

# PIL 라이브러리로 이미지 불러오기 [jpg 파일도 가능]
pil_image= Image.open('Projects/images/newyork.jpg') #이미지 모듈로 이미지 여는방법임
#사이즈 조정
pil_image= pil_image.resize( (300,250), Image.LANCZOS  ) #사이즈를 튜플로.., 품질옵션 야 필 이미지야 너 리사이즈좀 해봐라는 말임. 튜플로 줘야함 그리고 뒤에는 옵션을 쓰는것임 LANCZOS 이건 품질옵션기능임)
# pillow image를 tikiner용 image로 변환
img2= ImageTk.PhotoImage(image=pil_image) #제이피지를 필로우로 먼저 읽어, 그걸 티킨터 용으로 만들어줘라는 단계가 추가된것임

#이미지 액자에 사진 보여주기
label2= Label(window, image=img2) #액자가 레이블이라고 생각하면 됨 사진을 액자에 감싸서 팩 뽑아라는 뜻임.
label2.pack()

# 버튼 클릭할때 이미지 변경해보기..
# 변경될 이미지를 미리 준비하기
pil_image= Image.open('Projects/images/ms19.png') #아까처럼 이미지에게 열어, -> 이미지 19번 이라는 말임.
pil_image= pil_image.resize( (300,250), Image.LANCZOS ) #필로우 이미지는 사이즈가 크니까 리 사이즈를 해줘 300,250으로 그리고 뭔지 모르겠지만 이미지 품질을 좋게 해주는 기능이 있대 랜조스)
img3= ImageTk.PhotoImage(image=pil_image)

def eee():
    img= label2.cget('image') # image 속성값 취득
    if img == str(img2):
        label2.configure(image=img3)
    else:
        label2.configure(image=img2)

btn= Button(text='change image', command=eee)
btn.pack()


window.mainloop()