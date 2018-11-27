class Entity:
    def __init__(self, conditions, rect):
        self.conditions = conditions
        self.rect = rect
 
    def check_event(self, event):
        pass
 
    def draw(self, screen):
        pass
 
    def collide_with(self, second_entity):
        pass