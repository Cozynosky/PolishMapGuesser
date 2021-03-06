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
        while True: 
            if not self.gameOver:
                self.updateTime()
                time_delta = self.clock.tick(60) / 1000.0
                self.draw()
                self.inputManage()
                self.manager.update(time_delta)
                pygame.display.update()
            if self.gameOver:
                self.draw()
                self.inputManage()
                pygame.display.update()
            self.clock.tick(60)
                
    def newGame(self):
        self.clock = pygame.time.Clock()
        self.text_input = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=Rect(20, 20, 200, 100), manager=self.manager)
        self.text_input.focus()
        self.toGuess = [Province(province) for province in settings._PROVINCES]
        self.Guessed = []
        self.gameOver = False
        self.tries = 0
        self.startTime = pygame.time.get_ticks()

    def inputManage(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_input:
                        self.checkGuess(self.text_input.get_text().lower().strip())
                        self.text_input.set_text("")
                        self.tries += 1
            if event.type == KEYDOWN:
                if event.key == K_RETURN and self.gameOver:
                    self.gameOver = False
                    self.newGame()
            self.manager.process_events(event)
    
    def draw(self):
        self.window.blit(settings._BGIMAGE,(0,0))
        self.window.blit(settings._PROVINCESIMAGE,(0,0))
        for guessed in self.Guessed:
            self.window.blit(guessed.image,(0,0))
        self.showInfoBar()
        self.manager.draw_ui(self.window)
        if self.gameOver:
            self.drawGameOver()
    
    def checkGuess(self,guess):
        guess = guess.replace("-","")
        for prov in self.toGuess:
            if prov.name == guess:
                prov.image = settings._GUESSEDPROVINCESIMAGES[prov.name]
                self.Guessed.append(prov)
                self.toGuess.remove(prov)
                if len(self.toGuess) == 0:
                    self.text_input.unfocus()
                    self.gameOver = True
    
    def showInfoBar(self):
        infoSur = pygame.Surface((350,50))
        infoSur.fill((0,0,0))
        pygame.draw.rect(infoSur,(255,255,255),pygame.Rect(2,2,346,46))
        pygame.font.init()
        font = pygame.font.SysFont("Segoe UI",30)
        text = font.render(f"Tries: {self.tries}    Time: {self.minutes}:{self.seconds}",True,(0,0,0))
        infoSur.blit(text,(6,2))
        self.window.blit(infoSur,(350,20))
    
    def drawGameOver(self):
        self.window.blit(settings._CORRECTPROVINCESIMAGE,(0,0))
        font = pygame.font.SysFont("Segoe UI",40)
        text = font.render("Press -ENTER- to start a new game",True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = self.window.get_rect().center
        self.window.blit(text,textRect)
      
    def updateTime(self):
        self.minutes = str((pygame.time.get_ticks() - self.startTime)//1000//60).zfill(2)
        self.seconds = str((pygame.time.get_ticks() - self.startTime)//1000%60).zfill(2)
class Province:
    def __init__(self,name):
        self.name = name