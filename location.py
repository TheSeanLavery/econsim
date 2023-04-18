import pygame

class Location:
    def __init__(self, x, y, name, description, town):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.town = town
        self.rect = pygame.Rect(x, y, 32, 32)
