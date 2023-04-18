#map_generation.py

import random
import pygame
from location import Location
from town import Town
from item import Item

def check_overlap(new_location, locations, buffer):
    buffered_rect = new_location.rect.inflate(buffer, buffer)
    for location in locations:
        if buffered_rect.colliderect(location.rect):
            return True
    return False

def generate_locations(buffer):
    locations = []
    for i in range(20):
        while True:
            x = random.randint(100, 700)
            y = random.randint(100, 500)
            name = f"Location {i + 1}"
            description = f"A randomly generated location {i + 1}"
            items = [Item(f"Item {i}", "Random item", random.randint(1, 50)) for i in range(random.randint(1, 5))]
            gold = random.randint(0, 1000)
            town = Town(name, description, items, gold)  # Create town with generated items and gold
            new_location = Location(x, y, name, description, town)  # Add town to the location

            if not check_overlap(new_location, locations, buffer):
                locations.append(new_location)
                town.location = new_location  # Set the location of the town
                break
    return locations


def location_clicked(mouse_x, mouse_y, locations):
    for location in locations:
        if location.rect.collidepoint(mouse_x, mouse_y):
            return location
    return None
