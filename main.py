import pygame
from rocket import Rocket
from rocket2 import Rocket2
from ball import Ball

sc = pygame.display.set_mode((1100, 900))
pygame.display.set_caption("Ping Pong")
clock=pygame.time.Clock()
bg = pygame.image.load('background.jpg')
bg_over = pygame.image.load('game_over.png')

rocket = Rocket(sc)
rocket2 = Rocket2(sc)
ball = Ball(sc)

game = True
game_lose = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                rocket2.move_up = True
            if event.key == pygame.K_UP:
                rocket2.move_down = True
            if event.key == pygame.K_s:
                rocket.move_up = True
            if event.key == pygame.K_w:
                rocket.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                rocket2.move_up = False
            if event.key == pygame.K_UP:
                rocket2.move_down = False
            if event.key == pygame.K_s:
                rocket.move_up = False
            if event.key == pygame.K_w:
                rocket.move_down = False
    clock.tick(60)
    sc.blit(bg, (0, 0))
    rocket.output()
    rocket.update_rocket()
    rocket2.output()
    rocket2.update_rocket()
    ball.output()
    ball.update_rocket(rocket, rocket2, sc, bg_over)
    pygame.display.update()
pygame.quit()

