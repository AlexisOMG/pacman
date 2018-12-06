import pygame
from entity import Entity

class Pacman(Entity):
    def __init__(self, conditions, rect, imgState = 0, speed = 1):
        super().__init__([], rect, imgState)
        self.speed = speed
        self.IsMoving = True
        self.allConditions = conditions
        self.conditions = []
        self.change_type(1) #Направление пакмана 0-вверх, 1-вправо, 2-вниз, 3-влево, 4-смерть.

    def change_type(self, type):
        self.type = type
        self.conditions = self.allConditions[type]

    def move(self):
        if self.type == 0:
            self.rect[1] += self.speed
        elif self.type == 1:
            self.rect[0] += self.speed
        elif self.type == 2:
            self.rect[1] -= self.speed
        elif self.type == 3:
            self.rect[0] -= self.speed
