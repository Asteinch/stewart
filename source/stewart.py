import pygame

class Stewart:

    def __init__(self, game):

        self.win = game.win

        self.stewart_sprite = pygame.image.load("./resource/stewart.png")

        self.x, self.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    def draw(self):

        self.win.blit(self.stewart_sprite, (self.x, self.y))

    def update(self):

        self.x, self.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]