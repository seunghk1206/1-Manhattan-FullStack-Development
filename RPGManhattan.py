import pygame
import random
from random import sample

pygame.init()

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

#walkRight[4] = 5번째 사진??? 0번째가 첫번째다!!!

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("MANhattan game project")

surface = pygame.image.load('Game/R1.png')
pygame.display.set_icon(surface)
run = True
is_blue = True

x = 50
y = 400

width = 64
height = 64 #size of chracter

velocity = 5
left = False
right = False
walkCount = 0 #standing 

isJump = False
jumpCount = 5

def drawGameWindow(): #캐릭터가 움직일때마다 모션 표현
    
    global walkCount # 글로벌 변수 =함수 안에서 불렸지만 밖에서도 쓰임

    screen.blit(bg,(0,0)) # 내뒤에 있는 사진 지우기용

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3],(x,y)) # //3 -> 나머지 값을 제외 한 몫
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1 
    else:
        screen.blit(char, (x,y))
        walkCount = 0
    pygame.display.update()

def drawGameWindowEvil(): #캐릭터가 움직일때마다 모션 표현
    
    global walkCount # 글로벌 변수 =함수 안에서 불렸지만 밖에서도 쓰임

    screen.blit(bg,(0,0)) # 내뒤에 있는 사진 지우기용

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3],(x,y)) # //3 -> 나머지 값을 제외 한 몫
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1 
    else:
        screen.blit(char, (x,y))
        walkCount = 0
    pygame.display.update()

clock = pygame.time.Clock()
while run:
    clock.tick(27) # 27 frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed = pygame.key.get_pressed()
    ##작은 칸을 넘어가야함. 50 < x < 66 
    if pressed[pygame.K_LEFT] and x > velocity: 
        x -= velocity
        left = True
        right = False # left일때 오른쪽 키를 누르면 절대 안되기 때문
        
    elif pressed[pygame.K_RIGHT] and x < 500 - width - 5: 
        x += velocity
        right = True
        left= False
    
    else: # If jus standing
        right = False
        left = False
        walkCount = 0
    if pressed[pygame.K_w]:
        x = 500
        y = 999
########## 캐릭터의 점프 ###########
    if not (isJump): 
        if pressed[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -5:    
            y -= (jumpCount * abs(jumpCount)) * 1
            jumpCount -= 1
        else:
            jumpCount = 5
            isJump = False
    
    movement = random.sample(range(1,2), 1)
    if movement == 1:
        x += velocity
        right = True
        left = False
    if movement == 2:
        x -= velocity
        right = False
        left = True
####################################
    drawGameWindow()
    
pygame.quit()