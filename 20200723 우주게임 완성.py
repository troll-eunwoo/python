import pygame as p
import random as r

p.init()#초기화
w=(255,255,255)#red,green,blue
size=(600,800)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
#비행기
p_image=p.image.load("plane.png")
p_rect=p_image.get_rect(left=250,top=700)
x=0
y=0
#배경
bg=p.image.load("universe.png")
#미사일
bullet=p.image.load("bullet.png")
b_list=[]
#적군
en=p.image.load("적군 비행기.png")
en_list=[]
for x in range(5):
    en_rect=en.get_rect(left=r.randint(0,500),top=10)
    en_list.append(en_rect)
#10.점수
font=p.font.SysFont("malgungothic",20)
score= 0
#놓친 적균 변수
lose=0
#게임오버 글자
font2=p.font.SysFont("malgungothic",50)
#폭발 이미지
bo=p.image.load("폭발.png")


while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_UP:
                y=-15
        
            if event.key==p.K_DOWN:
                y=15
        
            if event.key==p.K_RIGHT:
                x=15
        
            if event.key==p.K_LEFT:
                x=-15
            if event.key==p.K_SPACE:
                b_rect=bullet.get_rect(left=p_rect.left+36,top=p_rect.top)
                b_list.append(b_rect)

        if event.type==p.KEYUP:
            if event.key==p.K_UP:
                y=0
        
            if event.key==p.K_DOWN:
                y=0
        
            if event.key==p.K_RIGHT:
                x=0
        
            if event.key==p.K_LEFT:
                x=0

    p_rect.left+=x#+= --> p_rect.left=p_rect.left+x
    p_rect.top+=y
    if p_rect.left>=500:
        x =-15
    if p_rect.left<=0:
        x=15

    sc.fill(w)
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(bullet,b_rect)
    for b_rect in b_list:
        b_rect.top-=20
        if b_rect.top<=0:
            b_list.remove(b_rect)
            
        
    sc.blit(p_image,p_rect)

    for en_rect in en_list:
        sc.blit(en,en_rect)
    for en_rect in en_list:
        en_rect.top+=4
        if en_rect.top>=800:
            en_list.remove(en_rect)
            lose=lose+1
            en_rect=en.get_rect(left=r.randint(0,500),top=10)
            en_list.append(en_rect)
            


    for en_rect in en_list:
        for b_rect in b_list:
            if b_rect.colliderect(en_rect):
                en_list.remove(en_rect)
                sc.blit(bo,(en_rect))
                b_list.remove(b_rect)
                en_rect=en.get_rect(left=r.randint(0,500),top=10)
                en_list.append(en_rect)
                score=score+1
    

    text =font.render("점수:{}".format(score),True,(255,255,0))
    text2=font.render("놓친 적군 갯수:{}".format(lose),True,(255,255,0))
    text3=font2.render("GAME OVER",True,(255,0,0))
    sc.blit(text,(50,50))
    sc.blit(text2,(400,50))

    if lose>=20:
        sc.blit(text3,(175,400))
        playing=False
    


    
    p.display.flip()#화면 업데이트
