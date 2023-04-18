import pygame
from map_generation import location_clicked

def handle_event(event, current_town, locations):
    if event.type == pygame.QUIT:
        return False, current_town

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if current_town:
            if current_town.exit_button.collidepoint(mouse_x, mouse_y):
                current_town = None
        else:
            clicked_location = location_clicked(mouse_x, mouse_y, locations)
            if clicked_location:
                current_town = clicked_location.town
    return True, current_town
