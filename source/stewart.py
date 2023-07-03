import pygame

class Stewart:

    def __init__(self, game):

        self.win = game.win

        self.fire_group = pygame.sprite.Group()

        self.stewart_sprite = pygame.image.load("./resource/stewart.png")
        self.w, self.h = 200, 168

        self.x, self.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    def draw(self):

        self.win.blit(self.stewart_sprite, (self.x - self.w / 2, self.y - self.h / 2))
        

    def update(self):

        self.x, self.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]