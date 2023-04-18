import pygame
from location import Location
from town import Town
from item import Item
from map_generation import generate_locations

def location_clicked(mouse_x, mouse_y, locations):
    for location in locations:
        if location.rect.collidepoint(mouse_x, mouse_y):
            return location
    return None

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Overworld Map Game")

locations = generate_locations(50)

font = pygame.font.Font(None, 36)

running = True
current_town = None
def handle_event(event, current_town):
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

def draw_screen(screen, current_town, locations, font):
    screen.fill((0, 0, 0))

    if current_town:
        town_name_text = font.render(current_town.name, True, (255, 255, 255))
        town_desc_text = font.render(current_town.description, True, (255, 255, 255))
        exit_button_text = font.render("Exit", True, (255, 255, 255))

        screen.blit(town_name_text, (350, 200))
        screen.blit(town_desc_text, (350, 250))
        pygame.draw.rect(screen, (255, 0, 0), current_town.exit_button)
        screen.blit(exit_button_text, (375, 525))
    else:
        for location in locations:
            pygame.draw.rect(screen, (255, 255, 255), location.rect)

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        running, current_town = handle_event(event, current_town)

    draw_screen(screen, current_town, locations, font)

pygame.quit()
