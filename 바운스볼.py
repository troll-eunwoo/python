import pygame as p

p.init()
w =(255,255,255)
size = (1000,600)
sc = p.display.set_mode(size)
p.display.set_caption("바운스볼")
playing = True
#공 이미지
ball=p.image.load("공.png")
bg=p.image.load("배경.png")
#발판
pan=p.image.load("발판.png")
p_rect=pan.get_rect(left=0,top=450)
p_rect1=pan.get_rect(left=100,top=350)
p_rect2=pan.get_rect(left=200,top=250)
p_rect3=pan.get_rect(left=300,top=150)
p_rect4=pan.get_rect(left=400,top=50)
p_rect5=pan.get_rect(left=500,top=50)
p_rect6=pan.get_rect(left=600,top=150)
p_rect7=pan.get_rect(left=700,top=250)
p_rect8=pan.get_rect(left=800,top=350)

#목표
star=p.image.load("star.png")
s_rect=star.get_rect(left=870,top=400)
#game over
font=p.font.SysFont("malgungothic",50)
text=font.render("GAME OVER!",True,(255,0,0))

b_rect=ball.get_rect(left=0,top=00)
b_y=0
b_x=0
clock=p.time.Clock()

while playing:
    clock.tick(50) #초당 100개 화면이 지나
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                b_x=-5
            if event.key==p.K_RIGHT:
                b_x=5
        if event.type==p.KEYUP:
            if event.key==p.K_LEFT:
                b_x=0
            if event.key==p.K_RIGHT:
                b_x=0


    b_rect.left+=b_x       

    sc.fill(w)
    #배경
    sc.blit(bg,(0,0))
    sc.blit(ball,b_rect)
    sc.blit(pan,p_rect)

    if b_rect.colliderect(p_rect):
            b_y=-15
    if b_rect.colliderect(p_rect1):
            b_y=-15
    if b_rect.colliderect(p_rect2):
            b_y=-15
    if b_rect.colliderect(p_rect3):
            b_y=-15
    if b_rect.colliderect(p_rect4):
            b_y=-15
    if b_rect.colliderect(p_rect5):
            b_y=-15
    if b_rect.colliderect(p_rect6):
            b_y=-15
    if b_rect.colliderect(p_rect7):
            b_y=-15
    if b_rect.colliderect(p_rect8):
            b_y=-15
    if b_rect.colliderect(s_rect):
            playing=False

            
    b_rect.top+=b_y
    b_y+=1
    if b_rect.top>=570:
        sc.blit,(text,(450,250))
        playing = False

        
    #공 좌우 막아
    if b_rect.left<=0:
        b_rect.left=0
    if b_rect.left>=970:
        b_rect.left=970
        
    sc.blit(pan,p_rect)
    sc.blit(pan,p_rect1)
    sc.blit(pan,p_rect2)
    sc.blit(pan,p_rect3)
    sc.blit(pan,p_rect4)
    sc.blit(pan,p_rect5)
    sc.blit(pan,p_rect6)
    sc.blit(pan,p_rect7)
    sc.blit(pan,p_rect8)

    sc.blit(star,s_rect)

    
    p.display.flip()
