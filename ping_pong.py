from pygame import *
display.set_caption("пингпонг")
window = display.set_mode((700, 500))
background = transform.scale(image.load("1616544260_43-p-zhivoi-fon-54 — копия.jpg"), (700,500))

clock = time.Clock()

game = True

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick()