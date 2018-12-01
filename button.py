import pygame
from entity import Entity

class Button(Entity):
    def __init__(self, conditions, rect, function, imgState = 0):
        super().__init__(conditions, rect, imgState)
        self.function = function
        self.clicked = False #Если кнопка нажата - True, иначе - False

    def on_click(self):
        self.next_state()
        self.clicked = True

    def on_release(self):
        self.next_state()
        self.clicked = False
        self.function()

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.collide_with(event.pos):
                self.on_click()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked:
                self.on_release()
