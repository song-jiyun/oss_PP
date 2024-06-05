import pygame
import random

#기본 상수 정의
fps = 60                #게임의 fps
screen_width = 1920     #창 너비
screen_height = 1080    #창 높이
field_width = 9        #게임판 너비
field_height = 9       #게임판 높이
mines = 10              #지뢰 갯수
#기본 상수 정의

#색상 정의
black = (0, 0, 0)           #8
white = (255, 255, 255)
red = (255, 0, 0)           #7
redgreen = (255, 170, 0)    #6
greenred = (170, 255, 0)    #5
green = (0, 255, 0)         #4
greenblue = (0, 255, 170)   #3
bluegreen = (0, 170, 255)   #2
blue = (0, 0, 255)          #1
#색상 정의

#게임판
field = []          #숫자와 지뢰의 위치정보, 0~8은 주변칸의 지뢰 갯수, 9는 지뢰
field_cover = []    #가림막 정보, 0은 공개된 위치, 1은 가려진 위치
#게임판

#해당 칸의 지뢰 여부 판별
def ismine(x, y):
    return (field[x][y] == 9)
#해당 칸의 지뢰 여부 판별

#주변의 지뢰 갯수 세기
def countmine(x, y):
    count = 0
    if(x != 0):
        if(ismine(x - 1, y)):
            count += 1

        if(y != 0):
            if(ismine(x - 1, y - 1)):
                count += 1
        
        if(y != field_height - 1):
            if(ismine(x - 1, y + 1)):
                count += 1

    if(x != field_width - 1):
        if(ismine(x + 1, y)):
            count += 1

        if(y != 0):
            if(ismine(x + 1, y - 1)):
                count += 1

        if(y != field_height - 1):
            if(ismine(x + 1, y + 1)):
                count += 1

    if(y != 0):
        if(ismine(x, y - 1)):
            count += 1

    if(y != field_height - 1):
        if(ismine(x, y + 1)):
            count += 1

    return count
#주변의 지뢰 갯수 세기

#게임판 만들기
def gameSetup():

    #게임판 0, 가림막 1로 초기화
    for x in range(0, field_width):
        field.append([])
        field_cover.append([])
        for y in range(0, field_height):
            field[x].append(0)
            field_cover[x].append(1)
    #게임판 0, 가림막 1로 초기화

    #지뢰 위치 설정
    i = 0
    while(i < mines):
        rand = random.randrange(0, field_width * field_height)
        x = rand // field_width
        y = rand % field_width
        if(field[x][y] == 9):
            continue
        i += 1
        field[x][y] = 9
    #지뢰 위치 설정

    #지뢰가 없는 칸에 주변 지뢰 갯수 입력
    for x in range(0, field_width):
        for y in range(0, field_height):
            if(field[x][y] != 9):
                field[x][y] = countmine(x, y)
    #지뢰가 없는 칸에 주변 지뢰 갯수 입력

#게임판 만들기

    
#게임 시작
pygame.init()
#while True:
gameSetup()

for x in range(0, field_width):
    print(field[x])
    
#게임 종료
pygame.quit()
