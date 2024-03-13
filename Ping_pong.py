from pygame import *
from random import randint
from time import time as tm
# from time import *
window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
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

p1 = Player('raketa.png',600,30,50,50,5)
p2 = Player('raketa.png',30,200,50,50,5)
font.init()
font2 = font.SysFont('Arial', 36)

finish = False
game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        p1.updateL()
        p2.updateR()
        p1.reset()
        p2.reset()
    display.update()
    clock.tick(165)
