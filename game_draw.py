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

def draw_screen(screen, current_town, locations, agents, font, selected_agent=None):  # Add selected_agent parameter
    # ... other parts of the code ...

    if selected_agent:
        draw_agent_stats(screen, font, selected_agent)

def draw_agent_stats(screen, font, agent):
    stats_modal = pygame.Rect(200, 150, 400, 300)
    pygame.draw.rect(screen, (200, 200, 200), stats_modal)

    text_lines = [
        f"GUID: {agent.guid}",
        f"Color: {agent.color}",
        f"Carry Weight Capacity: {agent.carry_weight_capacity}",
        f"HP: {agent.hp}",
        f"Level: {agent.level}",
        f"Speed: {agent.speed}",
        f"Items: {', '.join([item.name for item in agent.items])}",
        f"Gold: {agent.gold}"
    ]

    for idx, line in enumerate(text_lines):
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (210, 160 + idx * 30))