import pygame
import random
import time

#기본 상수 정의
fps = 60                #게임의 fps
field_width = 9        #게임판 너비
field_height = 9       #게임판 높이
mines = 10              #지뢰 갯수
tile_size = 40          #타일 크기
screen_width = tile_size * field_width     #창 너비
screen_height = tile_size * field_height    #창 높이
game_over = False
game_win = False
#기본 상수 정의

#색상 정의
black = (0, 0, 0)           #8
white = (255, 255, 255)
gray = (128, 128, 128)
red = (255, 0, 0)           #7
redgreen = (255, 170, 0)    #6
greenred = (170, 255, 0)    #5
green = (0, 255, 0)         #4
greenblue = (0, 255, 170)   #3
bluegreen = (0, 170, 255)   #2
blue = (0, 0, 255)          #1
yellow = (255, 255, 0)
#색상 정의

#게임판
field = []          #숫자와 지뢰의 위치정보, 0~8은 주변칸의 지뢰 갯수, 9는 지뢰
field_cover = []    #가림막 정보, 0은 공개된 위치, 1은 가려진 위치
########################################
############## phase 2_2 ###############
########################################
field_flags = []    # 깃발 정보, 0은 깃발 없는 기본 상태, 1은 깃발 있는 상태
########################################
############## phase 2_2 ###############
########################################
########################################
############## phase 2_3 ###############
########################################
field_hints = []
########################################
############## phase 2_2 ###############
########################################
#게임판

#해당 칸의 지뢰 여부 판별
def isMine(x, y):
    return (field[x][y] == 9)
#해당 칸의 지뢰 여부 판별

#주변의 지뢰 갯수 세기
def countMine(x, y):
    count = 0
    if(x != 0):
        if(isMine(x - 1, y)):
            count += 1

        if(y != 0):
            if(isMine(x - 1, y - 1)):
                count += 1
        
        if(y != field_height - 1):
            if(isMine(x - 1, y + 1)):
                count += 1

    if(x != field_width - 1):
        if(isMine(x + 1, y)):
            count += 1

        if(y != 0):
            if(isMine(x + 1, y - 1)):
                count += 1

        if(y != field_height - 1):
            if(isMine(x + 1, y + 1)):
                count += 1

    if(y != 0):
        if(isMine(x, y - 1)):
            count += 1

    if(y != field_height - 1):
        if(isMine(x, y + 1)):
            count += 1

    return count
#주변의 지뢰 갯수 세기

#게임판 만들기
def gameSetup():

    #게임판 0, 가림막 1로 초기화
    for x in range(0, field_width):
        field.append([])
        field_cover.append([])
        ########################################
        ############## phase 2_2 ###############
        ########################################
        field_flags.append([])
        ########################################
        ############## phase 2_2 ###############
        ########################################
        ########################################
        ############## phase 2_3 ###############
        ########################################
        field_hints.append([])
        ########################################
        ############## phase 2_2 ###############
        ########################################
        for y in range(0, field_height):
            field[x].append(0)
            field_cover[x].append(1)
            ########################################
            ############## phase 2_2 ###############
            ########################################
            field_flags[x].append(0)
            ########################################
            ############## phase 2_2 ###############
            ########################################
            ########################################
            ############## phase 2_2 ###############
            ########################################
            field_hints[x].append(0)
            ########################################
            ############## phase 2_2 ###############
            ########################################
    #게임판 0, 가림막 1로 초기화

    #지뢰 위치 설정
    i = 0
    while(i < mines):
        rand = random.randrange(0, field_width * field_height)
        x = rand // field_height
        y = rand % field_height
        if(field[x][y] == 9):
            continue
        i += 1
        field[x][y] = 9
    #지뢰 위치 설정

    #지뢰가 없는 칸에 주변 지뢰 갯수 입력
    for x in range(0, field_width):
        for y in range(0, field_height):
            if(field[x][y] != 9):
                field[x][y] = countMine(x, y)
    #지뢰가 없는 칸에 주변 지뢰 갯수 입력
#게임판 만들기

#게임종료
def gameover(win):
    global game_over, game_win
    game_over = True
    game_win = win
    for x in range(0, field_width):
        for y in range(0, field_height):
            if(isMine(x, y)):
                field_cover[x][y] = 0
#게임종료

#칸 열기
def uncover(x, y):
    
    #무한재귀 방지
    if(field_cover[x][y] == 0):
        return
    #무한재귀 방지

    field_cover[x][y] = 0

    #해당칸이 0이면 주변칸도 열어야 함
    if(field[x][y] == 0):
        if(x != 0):
            uncover(x - 1, y)

            if(y != 0):
                uncover(x - 1, y - 1)
        
            if(y != field_height - 1):
                uncover(x - 1, y + 1)

        if(x != field_width - 1):
            uncover(x + 1, y)

            if(y != 0):
                uncover(x + 1, y - 1)

            if(y != field_height - 1):
                uncover(x + 1, y + 1)

        if(y != 0):
            uncover(x, y - 1)

        if(y != field_height - 1):
            uncover(x, y + 1)
    #해당칸이 0이면 주변칸도 열어야 함
    
    #해당칸이 지뢰면 게임오버
    elif(isMine(x, y)):
        gameover(False)
    #해당칸이 지뢰면 게임오버
#칸 열기

########################################
############## phase 2_2 ###############
########################################
# 깃발 토글
def toggleFlag(x, y):
    if field_cover[x][y] == 1:
        if field_flags[x][y] == 0:
            field_flags[x][y] = 1
        else:
            field_flags[x][y] = 0
########################################
############## phase 2_2 ###############
########################################

########################################
############## phase 2_3 ###############
########################################
# 힌트 사용
def useHint(x, y):
    if field_cover[x][y] == 1 and field_hints[x][y] == 0:
        field_hints[x][y] = 1
        uncover(x, y)
########################################
############## phase 2_2 ###############
########################################

#승리 확인
def gameWin():
    for x in range(0, field_width):
        for y in range(0, field_height):
            if(field[x][y] != 9 and field_cover[x][y] == 1):
                return False
    return True
#승리 확인

########################################
############## phase 2_1 ###############
########################################
start_ticks = pygame.time.get_ticks()
########################################
############## phase 2_1 ###############
########################################

#게임 시작
pygame.init()                           #pygame 라이브러리 초기화
pygame.display.set_caption("minesweeper")  #창 제목 설정
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

gameSetup()

running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        elif(event.type == pygame.MOUSEBUTTONDOWN and not game_over):
            x, y = event.pos[0] // tile_size, event.pos[1] // tile_size
            if(0 <= x < field_width and 0 <= y < field_height):
                ########################################
                ############## phase 2_2 ###############
                ########################################
                if event.button == 1:  # 좌클릭
                    uncover(x, y)
                elif event.button == 3:  # 우클릭
                    toggleFlag(x, y)
                ########################################
                ############## phase 2_2 ###############
                ########################################
                ########################################
                ############## phase 2_3 ###############
                ########################################
                elif event.button == 2:
                    useHint(x, y)
                ########################################
                ############## phase 2_3 ###############
                ########################################

    screen.fill(black)
    for x in range(field_width):
        for y in range(field_height):
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            ########################################
            ############## phase 2_2 ###############
            ########################################
            if field_flags[x][y] == 1:  # 깃발 표시
                pygame.draw.rect(screen, yellow, rect)
                flag_text = pygame.font.Font(None, 24).render('F', True, black)
                screen.blit(flag_text, (x * tile_size + 12, y * tile_size + 8))
            ########################################
            ############## phase 2_3 ###############
            ########################################
            elif (field_hints[x][y] == 1):  # 힌트가 사용된 경우
                pygame.draw.rect(screen, white, pygame.Rect(x * tile_size + 3, y * tile_size + 3, tile_size - 6, tile_size - 6))  # 힌트 사용 위치는 밝은 흰색으로 표시
            ########################################
            ############## phase 2_3 ###############
            ########################################
            elif field_cover[x][y]:
                pygame.draw.rect(screen, white, rect)
            ########################################
            ############## phase 2_2 ###############
            ########################################
            else:
                color = gray
                pygame.draw.rect(screen, color, rect)
                number = field[x][y]
                if(isMine(x, y)):
                    if(game_win):
                        mine = 'O'
                        color = white
                    else:
                        mine = 'X'
                        color = red
                    text = pygame.font.Font(None, 24).render((mine), True, color)
                if(number > 0 and not isMine(x, y)):
                    if(number == 1):
                        text_color = blue
                    elif(number == 2):
                        text_color = bluegreen
                    elif(number == 3):
                        text_color = greenblue
                    elif(number == 4):
                        text_color = green
                    elif(number == 5):
                        text_color = greenred
                    elif(number == 6):
                        text_color = redgreen
                    elif(number == 7):
                        text_color = red
                    elif(number == 8):
                        text_color = black
                    text = pygame.font.Font(None, 24).render(str(number), True, text_color)
                if(number != 0):
                    screen.blit(text, (x * tile_size + 12, y * tile_size + 8))

    if(gameWin()):
        gameover(True)

########################################
############## phase 2_1 ###############
########################################
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = pygame.font.Font(None, 36).render(f'Time: {elapsed_seconds}', True, black)
    screen.blit(timer_text, (screen_width - 150, 10))
########################################
############## phase 2_1 ###############
########################################

    pygame.display.flip()
    clock.tick(fps)


#for x in range(0, field_width):
#    print(field[x])
    
#게임 종료
pygame.quit()