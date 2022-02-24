import pygame as p
import copy 
import random as r



p.init()
w =(255,255,255)
green=(0,255,0)
black=(0,0,0)
size = (800,600)
sc = p.display.set_mode(size)
p.display.set_caption("트롤 버티기 게임")

score=0
font=p.font.SysFont("malgungothic",20)

plane=p.image.load("트롤.png")
p_y=5
p_rect=plane.get_rect(left=10,top=150)
clock=p.time.Clock()

playing = True
#폭발
ex=p.image.load("놀란 트롤.png")

game_over=False

#동굴
rects=[]
for x in range(80):
    rect=p.Rect(x*10,100,10,400)
    rects.append(rect)

slope=2


while playing:
    clock.tick(15)#초당 30번 이미지를 보여줘(fps)
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_SPACE:
                p_y=-5
        if event.type==p.KEYUP:
            if event.key==p.K_SPACE:
                p_y=5

    sc.fill(green)
    
    p_rect.top+=p_y
    #배경 업로드
    for rect in rects:
        p.draw.rect(sc,black,rect)
    for rect in rects:
        rect.left=rect.left-10
    del rects[0]
        #추가 동굴 그리기
    new_rect=copy.deepcopy(rects[-1])
    new_rect.left=new_rect.left+10
    new_rect.top=new_rect.top+slope
    rects.append(new_rect)
    #동굴 위로올리기
    test_rect= copy.deepcopy(rects[-1])
    test_rect.top=test_rect.top+slope
    if test_rect.top<=0 or test_rect.bottom>=600:
        slope=r.randint(10,15) * (-1 if slope >0 else 1)
        new_rect.height=new_rect.height + -25




    
    #동굴 충돌 조건
    if p_rect.top<rects[0].top or p_rect.bottom>rects[0].bottom:
        game_over=True
        playing=False
        #만일 game_over

    
    
    sc.blit(plane,p_rect)
    #만일 game_over
    if game_over:
        ex_rect=ex.get_rect(left=p_rect.left-5,top=p_rect.top-5)
        sc.blit(ex,ex_rect)
        playing=False
        
    score+=1 #score=score+1
    text=font.render("점수:{}".format(score),True,(255,255,0))
    sc.blit(text,(10,0))
    p.display.flip()
