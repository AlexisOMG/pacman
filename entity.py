class Entity:
    def __init__(self, conditions, rect, imgState = 0):
        self.conditions = conditions
        self.rect = rect
        self.imgState = imgState

    def check_event(self, event):
        pass

    def next_state(self):
        self.imgState = (self.imgState + 1) % len(self.conditions)

    def draw(self, screen):
        screen.blit(self.conditions[self.imgState], self.rect)

    def collide_with(self, point): #Возвращает TRUE если точка соприкасается с ентити, в противном случае - FALSE
        checkCoordX = False
        checkCoordY = False

        if point[1] >= self.rect[1] and point[1] <= self.rect[1] + self.rect[3]: #проверка на соприкосновение по оси y
            checkCoordY = True
        if point[0] >= self.rect[0] and point[0] <= self.rect[0] + self.rect[2]: #проверка на соприкосновение по оси x
            checkCoordX = True

        return checkCoordX * checkCoordY
