from pygame import *
from random import randint
from time import time as tm
# from time import *
window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('kort.jpg'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_image),(self.w, self.h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

p1 = Player('raketa.png',620,30,50,50,5)
p2 = Player('raketa.png',30,200,50,50,5)
ball = GameSprite('green_ball.png',200,200,50,50,1)
font.init()
font2 = font.SysFont('Arial', 36)

finish = False
game = True
clock = time.Clock()
speed_x = 1
speed_y = 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        p1.updateL()
        p2.updateR()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        #ball.rect.x < 0
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        p1.reset()
        p2.reset()
        ball.reset()
    display.update()
    clock.tick(165)
