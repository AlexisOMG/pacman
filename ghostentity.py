import pygame
from entity import Entity

class Ghost(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__([], rect, imgState)
        self.allConditions = conditions
        self.conditions = []
        self.change_type(1) #Направление пакмана 0-вверх, 1-вправо, 2-вниз, 3-влево, 4-смерть.

    def change_type(self, type):
        self.type = type
        self.conditions = self.allConditions[type]

    def move(self, dx, dy):
        self.rect[0] += dx
        self.rect[1] += dy
