import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(600,800)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing=True

#판 이미지
pan=p.image.load("손.png")
p_rect=pan.get_rect(left=250,top=730)

x=0
y=0
#배경 선언
bg=p.image.load("bg.png")
#공
ball=p.image.load("공.png")
b_rect=ball.get_rect(left=250,top=400)
#공 속도
b_x=8
b_y=8
#게임 오버 문구
font=p.font.SysFont('malgungothic',50)

#벽돌
block=p.image.load("block.png")
block_list=[]
for x in range(10):
    for y in range(5):
        blo_rect=block.get_rect(left=60*x,top=50*y)
        block_list.append(blo_rect)

font2=p.font.SysFont("malgungothic",25)
score=0

while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                x=-10
        
            if event.key==p.K_RIGHT:
                x=10

        if event.type==p.KEYUP:
            if event.key==p.K_LEFT:
                x=0
        
            if event.key==p.K_RIGHT:
                x=0
    p_rect.left+=x
           
    
    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    if p_rect.left>=500:
        p_rect.left=500
    if p_rect.left<=0:
        p_rect.left=0
        # 공 업로드
    sc.blit(ball,b_rect)   
    b_rect.top+=b_y
    b_rect.left+=b_x
    
    if b_rect.top>=800:
        playing=False
        sc.blit(text,(150,400))
    if b_rect.top<=0:
        b_y=-b_y
    if b_rect.left>=600:
        b_x=-b_x
    if b_rect.left<=0:
        b_x=-b_x
    text=font.render("GAME OVER",True,(255,0,0))
    text2=font2.render("점수:{}".format(score),True,(255,255,0))
    text3=font.render("Clear",True,(0,200,0))

    for blo_rect in block_list:
        sc.blit(block,blo_rect)
#공,벽 충돌시
    for blo_rect in block_list:
        if b_rect.colliderect(blo_rect):
            score=score+1
            block_list.remove(blo_rect)
            b_y=-2

    if p_rect.colliderect(b_rect):
        b_y=-2
        sc.blit(text2,(0,750))

    if len(block_list)<=0:
        sc.blit(text3,(150,400))
        playing=False
    
    p.display.flip()#화면 업데이트
