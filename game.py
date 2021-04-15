#!/usr/bin/python3
"""
main Game file
"""

import pygame
from pygame.locals import *
import sys
import pygame_gui

import settings

class Game:
    #Game object initialising method
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PolishMapGuesser")
        self.window = pygame.display.set_mode((settings._WINDOW_WIDTH,settings._WINDOW_HEIGHT))
        self.manager = pygame_gui.UIManager((settings._WINDOW_WIDTH,settings._WINDOW_HEIGHT),"theme.json")
        self.newGame()
    
    def run(self):
        while not self.gameOver:
            time_delta = self.clock.tick(60) / 1000.0
            self.draw()
            self.inputManage()
            self.manager.update(time_delta)
            pygame.display.update()
                
    def newGame(self):
        self.clock = pygame.time.Clock()
        self.text_input = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=Rect(20, 20, 200, 100), manager=self.manager)
        self.text_input.focus()
        self.toGuess = [Province(province) for province in settings._PROVINCES]
        self.Guessed = []
        self.tries = 0
        self.gameOver = False

    def inputManage(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_input:
                        self.checkGuess(self.text_input.get_text().lower())
                        self.text_input.set_text("")
                        self.tries += 1
            self.manager.process_events(event)
    
    def draw(self):
        self.window.blit(settings._BGIMAGE,(0,0))
        self.window.blit(settings._PROVINCESIMAGE,(0,0))
        for guessed in self.Guessed:
            self.window.blit(guessed.image,(0,0))
        self.manager.draw_ui(self.window)
    
    def checkGuess(self,guess):
        for prov in self.toGuess:
            if prov.name == guess:
                prov.image = settings._GUESSEDPROVINCESIMAGES[prov.name]
                self.Guessed.append(prov)
                self.toGuess.remove(prov)
                if len(self.toGuess) == 0:
                    pygame.time.wait(100)
                    self.gameOver = True

class Province:
    def __init__(self,name):
        self.name = name