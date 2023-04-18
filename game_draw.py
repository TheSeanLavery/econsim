import pygame

def draw_screen(screen, current_town, locations, agents, font):
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

        # Draw agents on the overworld
        for agent in agents:
            agent_x, agent_y = agent.agent_position()
            agent_color = agent.color
            pygame.draw.circle(screen, agent_color, (agent_x, agent_y), 5)

    pygame.display.flip()

    

def move_agents(agents, locations, delta_time):  # Add delta_time parameter
    for agent in agents:
        destination = agent.choose_new_location([location.town for location in locations])
        agent.move_towards_destination(destination, delta_time)

