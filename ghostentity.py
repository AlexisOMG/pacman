import pygame
from entity import Entity
from math import fabs
import random

class Ghost(Entity):
    def __init__(self, conditions, rect, imgState = 0, speed = 1):
        super().__init__([], rect, imgState)
        self.speed = speed
        self.allConditions = conditions
        self.conditions = []
        self.change_type(1) #Направление пакмана 0-вверх, 1-вправо, 2-вниз, 3-влево, 4-смерть.
        self.target = [0, 0]
        self.target_achieved = True

    def change_type(self, type):
        self.type = type
        self.conditions = self.allConditions[type]

    def move(self, dx, dy):
        self.rect[0] += dx
        self.rect[1] += dy
        
        
    def move_to_point(self):
        if not self.target_achieved:
            if self.target[0] == self.rect[0] and self.target[1] == self.rect[1]:
                self.target_achieved = True
            else:
                dx = self.target[0] - self.rect[0]
                dy = self.target[1] - self.rect[1]
                if fabs(dy) != 0:
                    self.rect[1] += dy // int(fabs(dy))
                elif dx != 0:
                    self.rect[0] += dx // int(fabs(dx))

    def start_moving_to_point(self, point):
        self.target[0] = point[0] - 10
        self.target[1] = point[1] - 10
        self.target_achieved = False
        
    def choose_target(self, vertex, graph):
        vertexes = graph.adjVertex[vertex]
        choosenVertex = vertexes[random.randint(0, len(vertexes) - 1)]
        self.target = [graph.coordinates[choosenVertex][0], graph.coordinates[choosenVertex][1]]
        self.target_achieved = False
        self.start_moving_to_point(self.target)
        return choosenVertex
        
    def check_target_achieved(self):
        return self.target_achieved
        

    '''def move_to_point(self, point):
        self.target = point
        if self.rect[0] != self.target[0] or self.rect[1] != self.target[1]:
            dx = self.target[0] - self.rect[0]
            dy = self.target[1] - self.rect[1]
            self.rect[0] += dx
            self.rect[1] += dy'''
        
