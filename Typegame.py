# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 15:43:22 2018

@author: Administrator
"""

import sys,random,time,pygame
from pygame.locals import *

def print_text(font,x,y,text,color = (255,255,255),shadow = True):
    if shadow:
        imgText = font.render(text,True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))
    
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Keyboard Demo")
font1 = pygame.font.Font(None,24)
font2 = pygame.font.Font(None,200)

white = 255,255,255
yellow = 255,255,0

key_flag = False
correct_answer = random.randint(97,122) 
seconds = 11
score = 0
clock_start = 0
game_over = True

x = random.randint(100,400)
y = random.randint(200,380)
color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False
        
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            clock_start = time.clock()
    
    current = time.clock() - clock_start
    speed = score * 6
    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97,122)
            score += 1
            x = random.randint(100,400)
            y = random.randint(200,380)
            color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    screen.fill((150,150,50))
    
    print_text(font1,0,0,"Mrs Hu,see how fast you can?")
    print_text(font1,0,20,"Keep up for 10 seconds~")
    
    
    if key_flag:
        print_text(font1,500,0,"<key>")
    
    if not game_over:
        print_text(font1,0,80,"Time: "+str(int(seconds - current)))
    print_text(font1,0,100,"Speed: "+str(speed)+"word/min")
    
    if game_over:
        print_text(font1,0,160,"Press Enter to Start!")
    print_text(font2,x,y,chr(correct_answer - 32),color)
    pygame.display.update()
