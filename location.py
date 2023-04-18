# location.py

import pygame
from town import Town

class Location:
    def __init__(self, x, y, name, description):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, 32, 32)
        self.town = Town(name, description, self)  # Pass self as the location object
