import math
import random
import uuid

import pygame
from item import Item

class Agent:
    def __init__(self, current_town, guid=None, color=None, carry_weight_capacity=None, hp=None, level=None, speed=None, items=None, gold=None):
        self.current_town = current_town
        self.guid = guid or str(uuid.uuid4())
        self.color = color or (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.carry_weight_capacity = carry_weight_capacity or random.randint(50, 150)
        self.hp = hp or random.randint(50, 100)
        self.level = level or random.randint(1, 10)
        self.speed = speed or random.uniform(0.5, 2)
        self.items = items or [Item(f"Item {i}", "Random item", random.randint(1, 50)) for i in range(random.randint(1, 5))]
        self.gold = gold or random.randint(0, 1000)
        self.position = self.current_town.location.x, self.current_town.location.y
        self.destination = self.current_town.location.x, self.current_town.location.y
        self.radius = 5 

    def choose_new_location(self, towns):
        current_x, current_y = self.position
        dest_x, dest_y = self.destination
        distance = math.sqrt((current_x - dest_x) ** 2 + (current_y - dest_y) ** 2)

        if distance < 1.0:
            new_town = random.choice(towns)
            center_x, center_y = new_town.location.rect.center
            self.destination = center_x, center_y
        return self.destination
    
    def agent_position(self):
        return self.position
    
    def move_towards_destination(self, destination, delta_time, speed=100):
        dest_x, dest_y = destination
        current_x, current_y = self.position

        distance_x = dest_x - current_x
        distance_y = dest_y - current_y

        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if distance <= 1.0:
            return

        normalized_x = distance_x / distance
        normalized_y = distance_y / distance

        move_x = normalized_x * speed * delta_time
        move_y = normalized_y * speed * delta_time

        new_x = current_x + move_x
        new_y = current_y + move_y

        self.position = new_x, new_y
        
    def contains_point(self, point):
        agent_rect = pygame.Rect(self.position[0] - self.radius, self.position[1] - self.radius, self.radius * 2, self.radius * 2)
        return agent_rect.collidepoint(point)
    
def agent_clicked(mouse_x, mouse_y, agents):
    for agent in agents:
        if agent.contains_point((mouse_x, mouse_y)):
            return agent
    return None