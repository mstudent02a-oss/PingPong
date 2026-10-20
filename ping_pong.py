#комментарий
from pygame import *

back = (200, 255, 255)
window = display.set_mode((900, 600))
display.set_caption('Ping pong')
window.fill(back)
clock = time.Clock()
FPS = 60

class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w, h, x, y, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h
        self.speed_x = speed_x
        self.speed_y = speed_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(Game_Sprite):
    def update(self):
        pass
        
ball = Player('ball_p.png', 50, 50, 400, 300, 5, 5)
p_left = Player('platform_v0.png', 30, 150, 20, 200, 0, 10)
p_right = Player('platform_v0.png', 30, 150, 850, 200, 0, 10)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        ball.reset()
        p_left.reset()
        p_right.reset()
    
    display.update()
    clock.tick(FPS)
