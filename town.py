# town.py

import random
import pygame

class Town:
    def __init__(self, name, description, items, gold):  # Add items and gold parameters
        self.name = name
        self.description = description
        self.location =  None
        self.exit_button = pygame.Rect(350, 520, 100, 40)
        self.items = items
        self.gold = gold
        #random color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

