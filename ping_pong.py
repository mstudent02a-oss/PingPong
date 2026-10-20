from pygame import *

font.init()
font1 = font.SysFont('Verdana', 70, 'bold')
lose = font1.render('GAME OVER', 1, (255, 0, 0))

back = (200, 255, 255)
win_width = 900
win_height = 600
window = display.set_mode((win_width, win_height))
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
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < win_height - self.rect.h:
            self.rect.y += self.speed_y
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.h:
            self.rect.y += self.speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > win_height - self.rect.h:
            self.speed_y *=-1
        
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
        window.fill(back)
        ball.reset()
        ball.update()
        p_left.reset()
        p_left.update_left()
        p_right.reset()
        p_right.update_right()
        
        if sprite.collide_rect(p_left, ball) or sprite.collide_rect(p_right, ball):
            ball.speed_x *= -1
            
        if ball.rect.x < 0 or ball.rect.x > win_width - ball.rect.w:
            #print('game over')
            window.blit(lose, (250, 250))
            
    
    display.update()
    clock.tick(FPS)
