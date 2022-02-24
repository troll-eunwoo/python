#가위 바위 보
import pygame as p
import random as r
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(1000,600)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("가위바위보게임")
playing=True
gawi=p.image.load("pngwing.com (48).png")
ga_rect=gawi.get_rect(left=800,top=100)

bawi=p.image.load("pngwing.com (49).png")
ba_rect=gawi.get_rect(left=800,top=250)

bo=p.image.load("pngwing.com (50).png")
bo_rect=gawi.get_rect(left=800,top=400)

vs=p.image.load("pngwing.com (57).png")
me=0
com=0

v="승리"
m="무승부"
f="패배"
mal="승패여부"
font=p.font.SysFont("malgungothic",45)
#나 컴 점수
my_v=0
com_v=0
font1=p.font.SysFont("malgungothic",35)




while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type==p.MOUSEBUTTONDOWN:
            if ga_rect.collidepoint(event.pos[0],event.pos[1]):
                me=1
                com=r.choice([1,2,3])
            if ba_rect.collidepoint(event.pos[0],event.pos[1]):
                me=2
                com=r.choice([1,2,3])
            if bo_rect.collidepoint(event.pos[0],event.pos[1]):
                me=3
                com=r.choice([1,2,3])
        print(me)

    sc.fill(w)
    sc.blit(gawi,ga_rect)
    sc.blit(bawi,ba_rect)
    sc.blit(bo,bo_rect)

    sc.blit(vs,(300,100))
    if me==1:
        sc.blit(gawi,(0,200))
        if com==1:
            mal=m
        if com==2:
            mal=f
            com_v += 1
            me = 4
        if com==3:
            mal=v
            my_v += 1
            me = 4
    if me==2:
        sc.blit(bawi,(0,200))
        if com==1:
            mal=v
            my_v += 1
            me = 5
        if com==2:
            mal=m
        if com==3:
            mal=f
            com_v+= 1
            me = 5
    if me==3:
        sc.blit(bo,(0,200))
        if com==1:
            mal=f
            com_v+=1
            me =6
        if com==2:
            mal=v
            my_v+=1
            me =6
        if com==3:
            mal=m
    if com==1:
        sc.blit(gawi,(600,200))
    if com==2:
        sc.blit(bawi,(600,200))
    if com==3:
        sc.blit(bo,(600,200))
    #버그 잡아
    if me == 4:
        sc.blit(gawi,(0,200))
    if me == 5:
        sc.blit(bawi,(0,200))
    if me ==6:
        sc.blit(bo,(0,200))
    

        #승패여부
    text=font.render("{}".format(mal),True,(0,0,0))
    sc.blit(text,(270,10))
    #승패 점수
    text_c=font1.render("이긴 횟수:{}".format(my_v),True,(0,0,0))
    text_m=font1.render("진 횟수:{}".format(com_v),True,(0,0,0))
    sc.blit(text_c,(100,100))
    sc.blit(text_m,(500,100))
    p.display.flip()#화면 업데이트
