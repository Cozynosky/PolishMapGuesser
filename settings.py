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
_PROVINCESIMAGES = {
    "dolnoslaskie": pygame.image.load("resources/background.png"),
    "kujawsko-pomorskie": pygame.image.load("resources/background.png"),
    "lubelskie": pygame.image.load("resources/background.png"),
    "lubuskie": pygame.image.load("resources/background.png"),
    "lodzkie": pygame.image.load("resources/background.png"),
    "malopolskie": pygame.image.load("resources/background.png"),
    "mazowieckie": pygame.image.load("resources/background.png"),
    "opolskie": pygame.image.load("resources/background.png"),
    "podkarpackie": pygame.image.load("resources/background.png"),
    "podlaskie": pygame.image.load("resources/background.png"),
    "pomorskie": pygame.image.load("resources/background.png"),
    "slaskie": pygame.image.load("resources/background.png"),
    "swietokrzyskie": pygame.image.load("resources/background.png"),
    "warminsko-mazurskie": pygame.image.load("resources/background.png"),
    "wielkopolskie": pygame.image.load("resources/background.png"),
    "zachodniopomorskie": pygame.image.load("resources/background.png"),
}
_GUESSEDPROVINCESIMAGES = {
    "dolnoslaskie": pygame.image.load("resources/background.png"),
    "kujawsko-pomorskie": pygame.image.load("resources/background.png"),
    "lubelskie": pygame.image.load("resources/background.png"),
    "lubuskie": pygame.image.load("resources/background.png"),
    "lodzkie": pygame.image.load("resources/background.png"),
    "malopolskie": pygame.image.load("resources/background.png"),
    "mazowieckie": pygame.image.load("resources/background.png"),
    "opolskie": pygame.image.load("resources/background.png"),
    "podkarpackie": pygame.image.load("resources/background.png"),
    "podlaskie": pygame.image.load("resources/background.png"),
    "pomorskie": pygame.image.load("resources/background.png"),
    "slaskie": pygame.image.load("resources/background.png"),
    "swietokrzyskie": pygame.image.load("resources/background.png"),
    "warminsko-mazurskie": pygame.image.load("resources/background.png"),
    "wielkopolskie": pygame.image.load("resources/background.png"),
    "zachodniopomorskie": pygame.image.load("resources/background.png"),
}
_PROVINCES = _PROVINCESIMAGES.keys()