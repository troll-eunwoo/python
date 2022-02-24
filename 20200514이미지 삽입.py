import pygame as p

p.init() #라이브러리 초기화

w=(255,255,255) #흰색

size=(500,500)
i=p.image.load("파인애플.png")
m=p.image.load("아보카도.png")
a=p.image.load("파이썬.png")
#음악 삽입
p.mixer.music.load("evolution.mp3")
p.mixer.music.play(0) #재생

sc=p.display.set_mode(size) #해상도 설정
p.display.set_caption("emage") #창제목

done=False

while not done:

    for event in p.event.get():#사용자가 뭘 누르는지 감지
        if event.type==p.QUIT: #게임창 x버튼을 누르면
           done=True #계속 반복 종료



    sc.fill(w) #배경화면 하얀색

    sc.blit(i,(60,200)) #이미지 화면 삽입
    sc.blit(m,(200,200)) #이미지 화면 삽입
    sc.blit(a,(340,200)) #이미지 화면 삽입
    p.display.flip() #화면 업데이트
        
    
