import pygame

from source.sky import *
from source.stewart import *
from source.deltatime import *

class Game:

    def __init__(self):

        self.win = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stewart")

        self.clock = pygame.time.Clock()

        self.setup()

    def setup(self):

        self.deltatime = deltatime()

        self.Sky = Sky(self)

        self.Stewart = Stewart(self)


    def update(self):

        self.deltatime.update()

        self.Sky.scroll(self.deltatime.dt)
        self.Stewart.update()

        pygame.display.update()
        self.clock.tick(60)

    def draw(self):

        self.win.fill((103, 231, 234))
        self.Sky.draw()
        self.Stewart.draw()

    def check_for_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def main_loop(self):

        while True:

            self.update()
            self.draw()
            self.check_for_input()

