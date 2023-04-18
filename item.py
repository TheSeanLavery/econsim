#item.py
import random
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
