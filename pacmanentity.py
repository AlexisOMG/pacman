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
        if self.IsMoving:
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
