#!/usr/bin/python3
"""
main Game file
"""

import pygame
from pygame.locals import *
import sys

import settings

class Game:
    #Game object initialising method
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((settings._WINDOW_WIDTH,settings._WINDOW_HEIGHT))
        self.newGame()
    
    def run(self):
        while True:
            self.inputManage()
            pygame.display.update()
            self.clock.tick(60)
    
    def newGame(self):
        self.clock = pygame.time.Clock()

    def inputManage(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()