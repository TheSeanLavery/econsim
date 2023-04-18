import pygame

class Town:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exit_button = pygame.Rect(350, 520, 100, 40)
