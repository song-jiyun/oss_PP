import pygame
import random

#기본 상수 정의
fps = 60                #게임의 fps
screen_width = 1920     #창 너비
screen_height = 1080    #창 높이
field_width = 24        #게임판 너비
field_height = 20       #게임판 높이
mines = 99              #지뢰 갯수

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

#게임 시작
pygame.init()
while True:
    
#게임 종료
pygame.quit()
