import pygame
from entity import Entity

class Pacman(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__([], rect, imgState)
        self.change_type(0) #Направление пакмана 0-вверх, 1-вправо, 2-вниз, 3-влево, 4-смерть.

    def change_type(self, type):
        self.type = type
        self.conditions = conditions[type]

    def move(self, dx, dy):
        self.rect[0] += dx
        self.rect[1] += dy
