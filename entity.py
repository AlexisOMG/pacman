class Entity:
    def __init__(self, conditions_, rect_):
        self.conditions = conditions_
        self.rect = rect_

    def check_event(self):
        pass

    def draw(self):
        pass

    def collide_with(self, second_entity):
        pass
