import pygame

def draw_screen(screen, current_town, locations, agents, font, clicked_agent=None):  # Add clicked_agent parameter
    screen.fill((0, 0, 0))
    if clicked_agent:
        draw_agent_popup(screen, clicked_agent, font)
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

# game_draw.py
def draw_agent_popup(screen, agent, font):
    text = f"GUID: {agent.guid}\nColor: {agent.color}\nCarry Weight Capacity: {agent.carry_weight_capacity}\nHP: {agent.hp}\nLevel: {agent.level}\nSpeed: {agent.speed}\nGold: {agent.gold}"
    text_lines = text.split("\n")
    max_width = max(font.size(line)[0] for line in text_lines)
    total_height = sum(font.size(line)[1] for line in text_lines) + (len(text_lines) - 1) * 5

    popup_surface = pygame.Surface((max_width + 20, total_height + 20), pygame.SRCALPHA)
    popup_surface.fill((128, 128, 128, 200))

    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, (255, 255, 255))
        popup_surface.blit(text_surface, (10, 10 + i * (font.size(line)[1] + 5)))

    agent_x, agent_y = agent.position
    screen.blit(popup_surface, (agent_x + 15, agent_y - 5))


