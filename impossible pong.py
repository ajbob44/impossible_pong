import pygame 
from pygame.locals import *
from random import randint
import time
pygame.init()

screen = pygame.display.set_mode([1500,300])

pygame.display.set_caption("impossible")
d = False
keep_going = True
WHITE = (255, 255, 255)
x = 1450
y = 150
xx = 50
yy = 150
up = False
down = False
w = False
s = False
xxx = 750
yyy = 150
xspeed = 8
yspeed = 8
player1 = 0
player2 = 0
a = 150
aa = 150
al = 0
hit = False
commove = 1
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            d = True
        if event.type == pygame.MOUSEBUTTONUP:
            d = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                down = True
            if event.key == K_UP:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                down = False
            if event.key == K_UP:
                up = False
    screen.fill((0, 0, 0))
    xxx = xxx + xspeed
    yyy = yyy + yspeed
    if yyy <= 3 or yyy >= 297:
        yspeed = yspeed * -1
    if xxx >= 1447:
        if yyy >= y and yyy <= y + 100:
            xspeed = abs(xspeed) * -1
    if xxx >= 1503:
        xxx = 750
        xspeed = xspeed * -1
        player1 =+1
        print('player 1 score =', player1)
        print('player 2 score =', player2)
    if xxx <= 73:
        if yyy >= yy and yyy <= yy + 100:
            xspeed = abs(xspeed)
            hit = True
    if xxx <= -3:
        xxx = 750
        xspeed = xspeed * -1
        player2 =+1
        print('player 1 score =', player1)
        print('player 2 score =', player2)
    if up:
        y = y - 1
    if down:
        y = y + 1
    if hit:
        a = yyy
        al = yspeed
        commove = 1500 - xxx
        for i in range(int(commove/abs(yspeed))):
            a = a + al
            if a <= 3 or a >= 297:
                al = al * -1
        commove = 750 - 73
        for i in range(int(commove/abs(yspeed))):
            a = a + al
            if a <= 3 or a >= 297:
                al = al * -1
    if xspeed < 0:
        a = yyy
        al = yspeed
        commove = xxx - 73
        for i in range(int(commove/abs(yspeed))):
            a = a + al
            if a <= 3 or a >= 297:
                al = al * -1
    if a > yy + 50:
        yy = yy + 1
    if a < yy + 50:
        yy = yy - 1
    pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 100), 2)
    pygame.draw.rect(screen, WHITE, pygame.Rect(xx, yy, 20, 100), 2)
    pygame.draw.circle(screen, WHITE, (xxx, yyy), 5)
    pygame.display.update()
    hit = False
    time.sleep(0.01)


pygame.quit()