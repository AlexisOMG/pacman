import sys
sys.path.append('./Entity/GameGraph/')
import pygame
import random
from constants import STATES, GAMEPLAY_STATES
from button import Button
from gamefield import GameField
from createGraph import Graph
from pacmanentity import Pacman
from fruit import Fruit
from seed import Seed

class game():
    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.objects = []
        self.immediately_close = False
        self.state = STATES["menu"]
        self.game_state = GAMEPLAY_STATES["level_1"]
        self.set_menu()
        self.graph = Graph()
        self.start_v = 0
        self.finish_v = 0
        self.turn_left = False
        self.turn_right = False
        self.turn_up = False
        self.turn_down = False

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.immediately_close = True
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.set_menu()
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.objects[1].change_type(0)
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.objects[1].change_type(3)
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                self.objects[1].change_type(2)
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                self.objects[1].change_type(1)
            for object in self.objects:
                object.check_event(event)
    
    def genPacmanImg(self):
        conditions = []
        conditions.append([])
        for i in range(3):
            conditions[0].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman" + str(i + 1) + "Up.png"), (20, 20)))
        conditions[0].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman2Up.png"), (20, 20)))
        conditions.append([])
        for i in range(3):
            conditions[1].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman" + str(i + 1) + "Right.png"), (20, 20)))
        conditions[1].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman2Right.png"), (20, 20)))
        conditions.append([])
        for i in range(3):
            conditions[2].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman" + str(i + 1) + "Down.png"), (20, 20)))
        conditions[2].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman2Down.png"), (20, 20)))
        conditions.append([])
        for i in range(3):
            conditions[3].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman" + str(i + 1) + "Left.png"), (20, 20)))
        conditions[3].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacman2Left.png"), (20, 20)))
        conditions.append([])
        for i in range(11):
            conditions[4].append(pygame.transform.scale(pygame.image.load("./Entity/Pacman/pacmanDie" + str(i + 1) + ".png"), (20, 20)))
        return conditions
            
    
    def set_menu(self):
        self.state = STATES["menu"]
        self.objects = []
        self.objects.append(Button([pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonNotPressed.png"), (100, 25)),
                                    pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonPreesed.png"), (100, 25))],
                                    [self.screen_size[0] // 2 - 50, self.screen_size[1] / 2 - 60, 100, 25], self.set_game))
        self.objects.append(Button([pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonSettings.png"), (100, 25)),
                                    pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonSettingsPresed.png"), (100, 25))],
                                    [self.screen_size[0] // 2 - 50, self.screen_size[1] / 2 - 30, 100, 25], self.set_settings))
        self.objects.append(Button([pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonExitNotPresed.png"), (100, 25)),
                                    pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonExitPresed.png"), (100, 25))],
                                    [self.screen_size[0] // 2 - 50, self.screen_size[1] / 2, 100, 25], self.set_exit))
    def set_game(self):
        self.state = STATES["game"]
        self.objects = []
        self.objects.append(GameField([pygame.transform.scale(pygame.image.load("./Entity/Map.png"),
                                        (424, 468))], [0, 0, 424, 468]))
        self.objects.append(Pacman(self.genPacmanImg(), [12, 10, 20, 20], 0, 1))
        self.start_v = 0
        self.finish_v = 1
        cnt = -1
        for v in self.graph.coordinates:
            cnt += 1
            if cnt < 28 or cnt > 30:
                name_on = "./Entity/Fruit/ SeedOn.png"
                name_off = "./Entity/Fruit/seedOff.png"
                self.objects.append(Seed([[pygame.transform.scale(pygame.image.load(name_on), (2, 2))],
                                         [pygame.transform.scale(pygame.image.load(name_off), (2, 2))]],
                                         [v[0] - 1, v[1] - 1, 2, 2]))

##        for v in self.graph.coordinates:     # генерация фруктов
##            cnt += 1
##            if ( 28 <= cnt <= 30):
##                continue
##            else:
##                i = random.randint(1, 5)
##                name = "./Entity/Fruit/fruit" + str(i) + ".png"
##                self.objects.append(Fruit([pygame.transform.scale(pygame.image.load(name), (15, 15))], [v[0] - 5, v[1] - 8, 10, 10]))

    def set_settings(self):
        self.state = STATES["settings"]
        self.objects = []

    def set_exit(self):
        self.immediately_close = True

    def loop(self):
        self.screen.fill((0, 0, 0))
        for object in self.objects:
            object.draw(self.screen)
        #if self.state == STATES["game"]:
            # for v in self.graph.coordinates:                     ##Рисует вершины графа для проверки
            #      pygame.draw.circle(self.screen, (0, 255, 0), v, 1)

        pygame.display.flip()

    def game_logic(self):
        if self.state == STATES["game"]:
            self.objects[1].move()

    def next_state(self):
        if self.state == STATES["game"]:
            for el in self.objects:
                el.next_state()

    def eat_seed(self):
        pass

    def check_finish(self):
        pass
