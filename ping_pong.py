from pygame import *

font.init()
font2 = font.SysFont("impact", 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.direction = "right"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
             self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 150:
             self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
             self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 150:
             self.rect.y += self.speed

left_r= Player("r.png",30,50,75,350,5)
right_r = Player("r.png",600,50,75,350,5)



display.set_caption("пингпонг")
window = display.set_mode((700, 500))
background = transform.scale(image.load("1616544260_43-p-zhivoi-fon-54 — копия.jpg"), (700,500))

finish = False

FPS = 60

clock = time.Clock()

game = True

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    left_r.reset()
    left_r.update_l()

    right_r.reset()
    right_r.update_r()


    display.update()
    clock.tick()
