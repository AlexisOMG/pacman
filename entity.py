class Entity:
    def __init__(self, conditions, rect):
        self.conditions = conditions
        self.rect = rect
 
    def check_event(self, event):
        pass
 
    def draw(self, screen):
        pass

    def collide_with(self, point): #Возвращает TRUE если точка соприкасается с ентити, в противном случае - FALSE
        checkCoordX = False
        checkCoordY = False
        
        if point.y >= self.rect.y and point.y <= self.rect.y + self.rect.height: #проверка на соприкосновение по оси y
            checkCoordY = True            
        if point.x >= self.rect.x and point.x <= self.rect.x + self.rect.width: #проверка на соприкосновение по оси x
            checkCoordX = True
            
        return checkCoordX * checkCoordY
