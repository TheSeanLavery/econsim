import pygame
from map_generation import location_clicked
from agent import agent_clicked  # Add this import

# Update the function signature to accept the agents list
def handle_event(event, current_town, locations, agents):
    if event.type == pygame.QUIT:
        return False, current_town, None

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if current_town:
            if current_town.exit_button.collidepoint(mouse_x, mouse_y):
                current_town = None
        else:
            clicked_location = location_clicked(mouse_x, mouse_y, locations)
            if clicked_location:
                current_town = clicked_location.town
            else:
                clicked_agent = agent_clicked(mouse_x, mouse_y, agents)  # Check for clicked agent
                if clicked_agent:
                    return True, current_town, clicked_agent
    return True, current_town, None
