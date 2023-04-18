import pygame
from location import Location
from town import Town
from item import Item
from map_generation import generate_locations, location_clicked
from agent import Agent
from game_event import handle_event
from game_draw import draw_screen, move_agents

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Overworld Map Game")

locations = generate_locations(50)
agents = [Agent(location.town) for location in locations]
font = pygame.font.Font(None, 36)

running = True
current_town = None

# ... other parts of the code ...


while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        running, current_town = handle_event(event, current_town, locations)

    move_agents(agents, locations, delta_time)  # Pass delta_time here
    draw_screen(screen, current_town, locations, agents, font)

pygame.quit()
