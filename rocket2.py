import pygame

class Rocket2(pygame.sprite.Sprite):
    def __init__(self, sc):
        pygame.sprite.Sprite.__init__(self)
        self.sc = sc
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.sc_rect = sc.get_rect()
        self.move_up = False
        self.move_down = False
        self.rect.centerx = 980
        self.rect.bottom = 600

    def output(self):
        self.sc.blit(self.image, self.rect)

    '''ПЕРЕМЕЩЕНИЕ'''
    def update_rocket(self):
        if self.move_up and self.rect.bottom < self.sc_rect.bottom:
            self.rect.centery += 4
        if self.move_down and self.rect.top > self.sc_rect.top:
            self.rect.centery -= 4