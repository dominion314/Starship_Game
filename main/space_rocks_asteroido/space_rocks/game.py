
"""
For details on specific lines of code, checkout realpythons page here:
https://realpython.com/asteroids-game-python/
"""

import pygame
from utils import load_sprite#this is calling the image from utils.py

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

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

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0,0))#This blit is what gives coordinates as two separate arguements for the surface you the machine to draw and where you want to draw it.
        pygame.display.flip()

from game import SpaceRocks #Takes care of creating a new instance of the game by runnning main_loop().

if __name__ == "__main__":
    space_rocks = SpaceRocks()
    space_rocks.main_loop()