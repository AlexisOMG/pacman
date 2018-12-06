import sys
sys.path.append('./Entity/GameGraph/')
import pygame
import random
from constants import STATES, GAMEPLAY_STATES
from button import Button
from gamefield import GameField
from createGraph import Graph
from fruit import Fruit

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
        cnt = -1
        for v in self.graph.coordinates:     # генерация фруктов
            cnt += 1
            if ( 28 <= cnt <= 30):
                continue
            else:
                i = random.randint(1, 5)
                name = "./Entity/Fruit/fruit" + str(i) + ".png"
                self.objects.append(Fruit([pygame.transform.scale(pygame.image.load(name), (15, 15))], [v[0] - 5, v[1] - 8, 10, 10]))

    def set_settings(self):
        self.state = STATES["settings"]
        self.objects = []

    def set_exit(self):
        self.immediately_close = True

    # def loop(self):
    #     self.screen.fill((0, 0, 0))
    #     for object in self.objects:
    #         object.draw(self.screen)
    #     if self.state == STATES["game"]:
    #         for v in self.graph.coordinates:                     ##Рисует вершины графа для проверки
    #              pygame.draw.circle(self.screen, (0, 255, 0), v, 1)

        pygame.display.flip()

    def game_logic(self):
        pass
