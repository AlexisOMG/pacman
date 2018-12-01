import pygame
from entity import Entity

class GameFill(Entity):
    def __init__(self, conditions, rect, imgState = 0):
        super().__init__(conditions, rect, imgState)
        