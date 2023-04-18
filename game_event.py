import pygame
import math
from map_generation import location_clicked

def handle_event(event, current_town, locations, agents):  # Add agents parameter
    clicked_agent = None

    if event.type == pygame.QUIT:
        return False, current_town, clicked_agent

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if current_town:
            if current_town.exit_button.collidepoint(mouse_x, mouse_y):
                current_town = None
        else:
            # Check if an agent was clicked
            for agent in agents:
                agent_x, agent_y = agent.position
                distance = math.sqrt((agent_x - mouse_x) ** 2 + (agent_y - mouse_y) ** 2)
                if distance < 10:  # Assuming the agent's size is 10 units
                    clicked_agent = agent
                    break

            if not clicked_agent:
                clicked_location = location_clicked(mouse_x, mouse_y, locations)
                if clicked_location:
                    current_town = clicked_location.town

    return True, current_town, clicked_agent  # Return clicked_agent as well
