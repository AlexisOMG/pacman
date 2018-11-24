class Entity:
    def __init__(self, conditions, rect):
        self.conditions = conditions
        self.rect = rect
 
    def check_event(self):
        pass
 
    def draw(self):
        pass
 
    def collide_with(self, second_entity):
        pass