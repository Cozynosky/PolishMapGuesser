#!/usr/bin/python3
"""
all settings and resources
"""
import pygame

# static settings
_WINDOW_WIDTH = 720
_WINDOW_HEIGHT = 720

# graphics
_BGIMAGE = pygame.image.load("resources/background.png")
_PROVINCESIMAGE = pygame.image.load("resources/toGuess.png")
_CORRECTPROVINCESIMAGE = pygame.image.load("resources/CorrectMap.png")
_GUESSEDPROVINCESIMAGES = {
    "dolnoslaskie": pygame.image.load("resources/dolnoslaskie.png"),
    "kujawskopomorskie": pygame.image.load("resources/kujpom.png"),
    "lubelskie": pygame.image.load("resources/lubelskie.png"),
    "lubuskie": pygame.image.load("resources/lubuskie.png"),
    "lodzkie": pygame.image.load("resources/lodzkie.png"),
    "malopolskie": pygame.image.load("resources/malopolskie.png"),
    "mazowieckie": pygame.image.load("resources/mazowieckie.png"),
    "opolskie": pygame.image.load("resources/opolskie.png"),
    "podkarpackie": pygame.image.load("resources/podkarpackie.png"),
    "podlaskie": pygame.image.load("resources/podlaskie.png"),
    "pomorskie": pygame.image.load("resources/pomorskie.png"),
    "slaskie": pygame.image.load("resources/slaskie.png"),
    "swietokrzyskie": pygame.image.load("resources/swietokrzyskie.png"),
    "warminskomazurskie": pygame.image.load("resources/warmaz.png"),
    "wielkopolskie": pygame.image.load("resources/wielkopolskie.png"),
    "zachodniopomorskie": pygame.image.load("resources/zachpom.png"),
}
_PROVINCES = _GUESSEDPROVINCESIMAGES.keys()