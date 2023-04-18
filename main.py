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


paused = False  # Add a paused variable to track the game state
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Overworld Map Game")

locations = generate_locations(50)
agents = [Agent(location.town) for location in locations]
font = pygame.font.Font(None, 36)

running = True
current_town = None

# ... other parts of the code ...


selected_agent = None

while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        running, current_town, selected_agent = handle_event(event, current_town, locations, agents)  # Update this line to handle the selected_agent

        if event.type == pygame.KEYDOWN:  # Check for key press events
            if event.key == pygame.K_SPACE:  # If the space key is pressed
                paused = not paused  # Toggle the paused state

    if not paused:
        move_agents(agents, locations, delta_time)

    # Move this line outside the event loop
    draw_screen(screen, current_town, locations, agents, font, selected_agent)  # Pass the selected_agent here


pygame.quit()
