import logic
import pygame
import pygame_gui
import sys

print(logic.make_new_problem())

class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def add(self, equation):
        if len(self.queue) <= self.capacity:
            self.queue.append(equation)
            return True
        return False
    
    def remove(self, index):
        if len(self.queue) - 1 >= index:
            return self.queue.pop(index)
        return None


# Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600))
clock = pygame.Clock()

test_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Hover Me',
    manager=manager
)

while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        manager.process_events(event)
        
        if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
            if event.ui_element == test_button:
                button_is_hovered = True
                
        if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
            if event.ui_element == test_button:
                button_is_hovered = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            if button_is_hovered:
                print("Success: Button is hovered and 'E' was pressed!")

    manager.update(time_delta)
    screen.fill("Purple")
    manager.draw_ui(screen)
    pygame.display.update()