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
        
        if point.y >= self.rect.y and point.y <= self.rect.y + self.rect.height: #проверка на соприкосновение по оси y
            checkCoordY = True            
        if point.x >= self.rect.x and point.x <= self.rect.x + self.rect.width: #проверка на соприкосновение по оси x
            checkCoordX = True
            
        return checkCoordX * checkCoordY
