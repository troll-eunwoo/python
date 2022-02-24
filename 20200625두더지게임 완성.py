import pygame as p
import random as r
import time as t

p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
ml=p.image.load("두더지.png")
ml_list=[]
for x in range(10):
    ml_rect=ml.get_rect(left=r.randint(0,700),top=r.randint(0,300))
    ml_list.append(ml_rect)

#점수표시
font=p.font.SysFont("malgungothic",20)
score=0
#남은시간
t1=int(t.time()) #멈춘시간

#효과음
p.mixer.init()#음악초기화
hit=p.mixer.Sound("총소리.wav")

while playing:
    t2=int(t.time()) #흐르는 시간
    timer= 30-(t2-t1)

    
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type==p.MOUSEBUTTONDOWN:
            for ml_rect in ml_list:
                if ml_rect.collidepoint(event.pos[0],event.pos[1]):
                    ml_list.remove(ml_rect)
                    ml_rect.left=r.randint(0,700)
                    ml_rect.top=r.randint(0,300)
                    ml_list.append(ml_rect)
                    score=score+1
                    hit.play()

    sc.fill(w)
    for ml_rect in ml_list:
        sc.blit(ml,ml_rect)

    text=font.render("점수:{}".format(score),True,(0,0,0))
    sc.blit(text,(370,0))

    text2=font.render("남은시간:{}".format(timer),True,(0,0,0))
    sc.blit(text2,(650,0))

    if timer==0:
        playing=False
        
    
        
    p.display.flip()#화면 업데이트
