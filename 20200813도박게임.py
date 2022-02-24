import pygame as p
import random as r


p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("도박게임")
playing=True

b=p.image.load("100.png")
b_rect=b.get_rect(left=600,top=45)
c=p.image.load("1000.png")
c_rect=b.get_rect(left=600,top=150)
m=p.image.load("10000.png")
m_rect=b.get_rect(left=600,top=250)
re=p.image.load("re.png")
r_rect=b.get_rect(left=10,top=300)
bg=p.image.load("bg12.png")
#글씨
money=10000
font=p.font.SysFont('malgungothic',30)
#확률 변수
box=0
#효과음
p.mixer.init()#믹서 라이브러리 초기화
give=p.mixer.Sound("돈딴거.wav")
lose=p.mixer.Sound("당황.wav")
empty=p.mixer.Sound("카페베네 효과.wav")

while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type==p.MOUSEBUTTONDOWN:
              if b_rect.collidepoint(event.pos):
                  box=r.choice([1,2,1,1,1])
                  if box == 1:
                      if money<=0:
                          empty.play()
                          print("돈부족")
                          break
                      else:
                          give.play()
                          money+=100
                  else:
                      if money<=0:
                          empty.play()
                          print("돈부족")
                          break
                      else:
                          lose.play()
                          money-=50
            
              if c_rect.collidepoint(event.pos):
                  box=r.choice([1,2,2,1,1])
                  if box == 1:
                      if money<=0:
                          empty.play()
                          print("돈부족")
                          break
                      else:
                          give.play()
                          money+=1000
                  else:
                      if money<=0:
                          empty.play()
                          print("돈부족")
                          break
                      else:
                          lose.play()
                          money-=500
              if m_rect.collidepoint(event.pos):
                  box=r.choice([1,2,2,2,1])
                  if box == 1:
                      if money<=0:
                          empty.play()
                          print("돈부족")
                          break
                      else:
                          give.play()
                          money+=10000
                  else:
                      if money<=0:
                          lose.play()
                          print("돈부족")
                          break
                      else:
                          money-=5000
              if r_rect.collidepoint(event.pos):
                    print("돈버는 아이콘")
                    money=money+10
    
    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(b,b_rect)
    sc.blit(c,c_rect)
    sc.blit(m,m_rect)
    sc.blit(re,r_rect)
    #돈 업로드
    text=font.render("돈:{}".format(money),True,(255,255,0))
    sc.blit(text,(0,0))
    p.display.flip()#화면 업데이트
