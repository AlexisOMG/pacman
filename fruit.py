import pygame
from entity import Entity

class Fruit(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__(conditions, rect)
        
    def getRect(self):
        return self.rect
