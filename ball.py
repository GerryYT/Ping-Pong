import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, sc):
        pygame.sprite.Sprite.__init__(self)
        self.sc = sc
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.sc_rect = sc.get_rect()
        self.move_up = False
        self.move_down = False
        self.rect.centerx = 550
        self.rect.bottom = 450
        self.speed_x = 6
        self.speed_y = 6

    def output(self):
        self.sc.blit(self.image, self.rect)

    '''ПЕРЕМЕЩЕНИЕ'''
    def update_rocket(self, rocket, rocket2, sc, bg_over):
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
        if pygame.sprite.collide_rect(rocket, self):
            self.speed_x = 6
        if pygame.sprite.collide_rect(rocket2, self):
            self.speed_x = -5
        if self.rect.bottom == self.sc_rect.bottom:
            self.speed_y *= -1
        if self.rect.right > self.sc_rect.right:
            sc.blit(bg_over, (380, 300))
        if self.rect.centery < self.sc_rect.top:
            self.speed_y *= -1
        if self.rect.left < self.sc_rect.left:
            sc.blit(bg_over, (380, 300))