import pygame

class Sky:

    def __init__(self, game):

        self.win = game.win

        self.sky_sprite = pygame.image.load("./resource/sky.png")

        self.sky1_y = -800
        self.sky2_y = -2400

        self.vel = 3

    def scroll(self, dt):
            
        self.sky1_y += self.vel * dt 
        self.sky2_y += self.vel * dt 

        self.sky1_y += self.vel * dt 
        self.sky2_y += self.vel * dt 
        if self.sky1_y >= 800:
            self.sky1_y = -2400
        if self.sky2_y >= 800:
            self.sky2_y = -2400
            


    def draw(self):

        self.win.blit(self.sky_sprite, (0, self.sky1_y))
        self.win.blit(self.sky_sprite, (0, self.sky2_y))