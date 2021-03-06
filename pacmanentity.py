import pygame
from entity import Entity
from math import fabs

class Pacman(Entity):
    def __init__(self, conditions, rect, imgState = 0, speed = 1):
        super().__init__([], rect, imgState)
        self.speed = speed
        self.IsMoving = True
        self.allConditions = conditions
        self.conditions = []
        self.change_type(1) #Направление пакмана 0-вверх, 1-вправо, 2-вниз, 3-влево, 4-смерть.
        self.target_achieved = True
        self.target = [0, 0]

    def change_type(self, type):
        self.type = type
        self.conditions = self.allConditions[type]

    def finish_dying(self):
        return (self.type == 4) and (self.imgState == len(self.conditions) - 1)

    def move_to_point(self):
        if not self.target_achieved:
            if self.target[0] == self.rect[0] and self.target[1] == self.rect[1]:
                self.target_achieved = True
            else:
                dx = self.target[0] - self.rect[0]
                dy = self.target[1] - self.rect[1]
                if fabs(dx) > fabs(dy):
                    self.rect[0] += dx // int(fabs(dx))
                else:
                    self.rect[1] += dy // int(fabs(dy))

    def start_moving_to_point(self, point):
        self.target = point
        self.target_achieved = False

    def get_type(self):
        return self.type

    def stop(self):
        self.IsMoving = False

    def start_moving(self):
        self.IsMoving = True

    def get_is_moving(self):
        return self.IsMoving

    def set_coordinates(self, x, y):
        self.rect[0], self.rect[1] = x, y


    def move(self):
        if self.IsMoving and self.target_achieved:
            if self.type == 0:
                self.rect[1] -= self.speed
            elif self.type == 1:
                self.rect[0] += self.speed
            elif self.type == 2:
                self.rect[1] += self.speed
            elif self.type == 3:
                self.rect[0] -= self.speed

    def collide_with(self, point): #Возвращает TRUE если точка соприкасается с ентити, в противном случае - FALSE
        checkCoordX = False
        checkCoordY = False
        rect = self.rect[:]
        ##rect[0] += self.rect[2] // 4
        ##rect[1] += self.rect[3] // 4
        ##rect[2] = rect[2] // 2
        ##rect[3] = rect[3] // 2

        if point[1] >= rect[1] and point[1] <= rect[1] + rect[3]: #проверка на соприкосновение по оси y
            checkCoordY = True
        if point[0] >= rect[0] and point[0] <= rect[0] + rect[2]: #проверка на соприкосновение по оси x
            checkCoordX = True

        return checkCoordX * checkCoordY
