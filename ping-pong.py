from pygame import *
mixer.init()
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
bg = transform.scale(image.load('table.png'),(700,500))
playerone = Player('rocketkaone.png',5,0,5,50,200)
playertwo = Player('rocketkatwo.png',5,650,5,50,200)
ball = Player('myach.png',5,350,250,50,50)
window = display.set_mode((700,500))
window.blit(bg,(0,0))
clock = time.Clock()

while game:
    window.blit(bg,(0,0))
    ball.reset()
    playerone.reset()
    playertwo.reset()
    playerone.update_right()
    playertwo.update_left()
    for e in event.get():
        if e.type == QUIT:
            game =False
    clock.tick(60)
    udar.play()
    display.update()
