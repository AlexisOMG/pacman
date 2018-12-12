import pygame
from entity import Entity

class Seed(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__([], rect, imgState)
        self.allConditions = conditions
        self.conditions = []
        self.change_type(0) #0 - семечко не съедено, 1 - семечко съедено


    def change_type(self, type):
        self.type = type
        self.conditions = self.allConditions[type]

    def getType(self):
        return self.type
