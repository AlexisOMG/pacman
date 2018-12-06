import sys
sys.path.append('./Entity/GameGraph/')
import pygame
from constants import STATES, GAMEPLAY_STATES
from button import Button
from gamefield import GameField
from createGraph import Graph
from pacmanentity import Pacman

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

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.immediately_close = True
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.set_menu()
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
        self.objects.append(Pacman(self.genPacmanImg(), [12, 10, 20, 20]))

    def set_settings(self):
        self.state = STATES["settings"]
        self.objects = []

    def set_exit(self):
        self.immediately_close = True

    def loop(self):
        self.screen.fill((0, 0, 0))
        for object in self.objects:
            object.draw(self.screen)
        if self.state == STATES["game"]:
            for v in self.graph.coordinates:                     ##Рисует вершины графа для проверки
                 pygame.draw.circle(self.screen, (0, 255, 0), v, 1)

        pygame.display.flip()

    def game_logic(self):
        if self.state == STATES["game"]:
            for el in self.objects:
                el.next_state()
            self.objects[1].move()
