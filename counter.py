import pygame
pygame.init()
class Counter():
    def __init__(self):
        my_file = open("hightScore.txt", 'r')
        self.hightScore = int(my_file.read())
        my_file.close()
        self.heals = 3
        self.level = 1
        self.points = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
    def draw(self, screen):
        text = self.font.render("Points " + str(self.points), 1, (255, 255, 255))
        screen.blit(text, (100, 100))

        text = self.font.render("Hight Score " + str(self.hightScore), 1, (255, 255, 255))
        screen.blit(text, (200, 100))

        text = self.font.render("Heal " + str(self.heals), 1, (255, 255, 255))
        screen.blit(text, (300, 100))

    def updatePoints(self, cnt):
        self.points += cnt
        updateHightScore()

    def updateHeals(self):
        self.heals -= 1

    def updateHightScore(self):
        if (self.points > self.hightScore):
            my_file = open("hightScore.txt", 'w')
            my_file.write(self.points)
            my_file.close()
