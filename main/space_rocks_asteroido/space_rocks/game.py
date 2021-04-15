
"""
For details on specific lines of code, checkout realpythons page here:
https://realpython.com/asteroids-game-python/
"""

import pygame

from models import Spaceship
from utils import load_sprite #this is calling the image from utils.py

class SpaceRocks: #Sets screen, background, and images. Displays them on screen according to coordinates.
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()#Controls speed of objects
        self.spaceship = Spaceship((400, 300)) 

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self): #Close the window b x-ing out or pressing escape key.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()

    def _process_game_logic(self):#This will update the frames as the objects move
        self.spaceship.move(self.screen)
        

    def _draw(self):#This will draw our objects and background.
        self.screen.blit(self.background, (0,0))#This blit is what gives coordinates as two separate arguements for the surface you the machine to draw and where you want to draw it.
        self.spaceship.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)#Controlls movement

from game import SpaceRocks #Takes care of creating a new instance of the game by runnning main_loop().

if __name__ == "__main__":
    space_rocks = SpaceRocks()
    space_rocks.main_loop()