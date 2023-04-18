import pygame
import random
import math

class Location:
    def __init__(self, x, y, name, description):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, 32, 32)

class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

def generate_locations():
    locations = []
    for i in range(20):
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        name = f"Location {i + 1}"
        description = f"A randomly generated location {i + 1}"
        location = Location(x, y, name, description)
        locations.append(location)
    return locations

def location_clicked(mouse_x, mouse_y, locations):
    for location in locations:
        if location.rect.collidepoint(mouse_x, mouse_y):
            return location
    return None

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Overworld Map Game")

locations = generate_locations()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_location = location_clicked(mouse_x, mouse_y, locations)
            if clicked_location:
                print(clicked_location.name, clicked_location.description)

    screen.fill((0, 0, 0))

    for location in locations:
        pygame.draw.rect(screen, (255, 255, 255), location.rect)

    pygame.display.flip()

pygame.quit()
