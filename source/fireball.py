import pygame

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./resource/fire.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 10

    def update(self):
        self.rect.y -= self.vel
        if self.rect.y < (-10):
            self.kill()   