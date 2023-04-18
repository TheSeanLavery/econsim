# location.py

import pygame
from town import Town

class Location:
    def __init__(self, x, y, name, description, town=None):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, 32, 32)
        self.town = town or Town(name, description, [], 0)  # Create a town with no items and no gold
