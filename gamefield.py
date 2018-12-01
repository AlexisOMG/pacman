import pygame
from entity import Entity

class GameField(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__(conditions, rect, imgState)
