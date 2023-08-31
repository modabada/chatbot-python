import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
font_large = pygame.font.SysFont('D2Coding', 72)
font = pygame.font.SysFont('D2Coding', 36)  # 폰트, D2Coding 은 노트북에 깔린 폰트
score = 0
isGameOver = False

img_girl = pygame.image.load('./avoid_bomb/girl.png')   # 소녀 이미지
img_bomb = pygame.image.load('./avoid_bomb/bomb.png')   # 폭탄 이미지
rect_girl = img_girl.get_rect(centerx=300, bottom=800)  # 소녀 위치정보
# generate bomb list by list comprehension
# 폭탄 위치정보 배열
ls_bomb = [img_bomb.get_rect(left= random.randint(0, 600 - 100), top = random.randint(0, 100)) for x in range(4)]

# toggle
left = False
right = False

while True:
    screen.fill((0, 0, 0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    # girl tirgger movement
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            left = True
        elif event.key == pygame.K_RIGHT:
            right = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left = False
        elif event.key == pygame.K_RIGHT:
            right = False
            
    
    # apply trigger
    if left:
        rect_girl.left -= 5
    if right:
        rect_girl.left += 5    
        
    # girl 좌우 범위 제한
    if rect_girl.left < 0:
        rect_girl.left = 0
    elif rect_girl.right > 600:
        rect_girl.right = 600
        
    # 폭탄 하강
    for e in ls_bomb:
        if e.colliderect(rect_girl):
            isGameOver = True
        e.top += 7
        # 만약 폭탄이 바닥까지 내려왔으면
        if e.top > 800:
            # 점수추가 후 위치 재설정
            if not isGameOver:
                score += 1
            e.left = random.randint(0, 600 - e.width)
            e.top = random.randint(0, 100)
        
    screen.blit(img_girl, rect_girl)    # girl 화면에 그림
    for e in ls_bomb:
        screen.blit(img_bomb, e)        # 폭탄들 화면에 그림
    # 점수 텍스트 표시
    screen.blit(font.render(f'점수: {score}', True, (255, 255, 0)), (10, 10))
    
    if isGameOver:
        txt = font_large.render(f'게임 오버', True, (255, 0, 0))
        screen.blit(txt, txt.get_rect(centerx = 300, centery = 400))
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()