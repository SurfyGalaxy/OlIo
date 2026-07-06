import logic
import pygame
import pygame_gui
import sys

class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.answers = []

    def add(self):
        if len(self.queue) <= self.capacity:
            equation = logic.make_new_problem()
            self.queue.append(equation)
            self.answers.append(eval(equation))
            return True
        return False
    
    def remove(self, index):
        if len(self.queue) - 1 >= index:
            self.queue.pop(index)
            self.answers.pop(index)
        return None

ram = RAM(10)
ram.add()

class Button:
    def __init__(self, relative_rect, text, manager, key):
        self.button = pygame_gui.elements.UIButton(
            relative_rect=relative_rect,
            text=text,
            manager=manager
        )
        self.key = key
        self.hovered = False
    
    def events(self, event):
        if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
            if event.ui_element == self.button:
                self.hovered = True
        
        if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
            if event.ui_element == self.button:
                self.hovered = False
        
        if event.type == pygame.KEYDOWN and event.key == self.key:
            if self.hovered:
                return True
        return False
    
    def change_text(self, text):
        self.button.set_text(text)


# Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()

button = Button(pygame.Rect((100, 100), (100, 100)), "", manager, pygame.K_e)

while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        manager.process_events(event)
        
        if button.events(event):
            button.change_text("NO")

    manager.update(time_delta)
    screen.fill("Purple")
    manager.draw_ui(screen)
    pygame.display.update()
