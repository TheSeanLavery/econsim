# town.py

import pygame

class Town:
    def __init__(self, name, description, location):  # Add location parameter
        self.name = name
        self.description = description
        self.location = location  # Store the location object
        self.exit_button = pygame.Rect(350, 520, 100, 40)
