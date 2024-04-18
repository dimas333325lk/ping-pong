from pygame import *
from random import *
mixer.init()
font.init()
udar = mixer.Sound('udar.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,im,sp,x,y,w = 80,h=100):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = sp
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y <300:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y <300:
            self.rect.y += self.speed

game=True
font1 = font.SysFont('Verdana',35)
lose2 = font1.render('Красный игрок пропустил мяч',True,(0,255,0))
lose1 = font1.render('Зелёный игрок пропустил мяч',True,(255,0,0))
finish = False
ballx=3
bally=3
klk = 0
bg = transform.scale(image.load('table.png'),(700,500))
playerone = Player('rocketkaone.png',5,650,5,50,200)
playertwo = Player('rocketkatwo.png',5,0,5,50,200)
ball = Player('myach.png',5,350,250,50,50)
window = display.set_mode((700,500))
window.blit(bg,(0,0))
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game =False
    if finish != True:
        window.blit(bg,(0,0))
        ball.rect.x += ballx
        ball.rect.y += bally
        if ball.rect.y > 450 or ball.rect.y <0:
            bally *= -1
            udar.play()
        if sprite.collide_rect(playerone,ball) or sprite.collide_rect(playertwo,ball):
            udar.play()
            ballx *= -1
            klk += 1
        if ball.rect.x <0:
            window.blit(lose1,(0,200))
            finish = True
        if ball.rect.x >650:
            window.blit(lose2,(0,200))
            finish = True
        if klk == 10:
            klk = 0
            ballx *=1.3
            bally *=1.3
        ball.reset()
        playerone.reset()
        playertwo.reset()
        playerone.update_right()
        playertwo.update_left()
    clock.tick(60)
    display.update()
