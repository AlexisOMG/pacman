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
from counter import Counter
from ghostentity import Ghost
from GameOver import GameOver

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
        self.counter = Counter()
        self.in_finish = False
        self.fruit_index = 0
        self.counterOfEatenFruits = 0
        self.gameover_exists = False

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.immediately_close = True
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.set_menu()
            if event.type == pygame.KEYUP and event.key == pygame.K_w and self.turn_up:
                if self.objects[1].get_type() != 0:
                    self.objects[1].change_type(0)
                    if not self.in_finish:
                        self.start_v, self.finish_v = self.finish_v, self.start_v
                    else:
                        self.objects[1].start_moving_to_point([self.graph.coordinates[self.finish_v][0] - 10,
                                                               self.graph.coordinates[self.finish_v][1] - 10])
                        ##self.objects[1].set_coordinates(self.graph.coordinates[self.finish_v][0] - 10,
                        ##                                self.graph.coordinates[self.finish_v][1] - 10)
            if event.type == pygame.KEYUP and event.key == pygame.K_a and self.turn_left:
                if self.objects[1].get_type() != 3:
                    self.objects[1].change_type(3)
                    if not self.in_finish:
                        self.start_v, self.finish_v = self.finish_v, self.start_v
                    else:
                        self.objects[1].start_moving_to_point([self.graph.coordinates[self.finish_v][0] - 10,
                                                               self.graph.coordinates[self.finish_v][1] - 10])
                        ##self.objects[1].set_coordinates(self.graph.coordinates[self.finish_v][0] - 10,
                        ##                                self.graph.coordinates[self.finish_v][1] - 10)
            if event.type == pygame.KEYUP and event.key == pygame.K_s and self.turn_down:
                if self.objects[1].get_type() != 2:
                    self.objects[1].change_type(2)
                    if not self.in_finish:
                        self.start_v, self.finish_v = self.finish_v, self.start_v
                    else:
                        self.objects[1].start_moving_to_point([self.graph.coordinates[self.finish_v][0] - 10,
                                                               self.graph.coordinates[self.finish_v][1] - 10])
                        ##self.objects[1].set_coordinates(self.graph.coordinates[self.finish_v][0] - 10,
                        ##                                self.graph.coordinates[self.finish_v][1] - 10)
            if event.type == pygame.KEYUP and event.key == pygame.K_d and self.turn_right:
                if self.objects[1].get_type() != 1:
                    self.objects[1].change_type(1)
                    if not self.in_finish:
                        self.start_v, self.finish_v = self.finish_v, self.start_v
                    else:
                        self.objects[1].start_moving_to_point([self.graph.coordinates[self.finish_v][0] - 10,
                                                               self.graph.coordinates[self.finish_v][1] - 10])
                        ##self.objects[1].set_coordinates(self.graph.coordinates[self.finish_v][0] - 10,
                        ##                                self.graph.coordinates[self.finish_v][1] - 10)
            for object in self.objects:
                object.check_event(event)
    
    def genPinkGhostImg(self):
        conditions = list()
        conditions.append([])
        conditions[0].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkUp1.png"),(20, 20)))
        conditions[0].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkUp2.png"),(20, 20)))
        conditions.append([])
        conditions[1].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkRight1.png"),(20, 20)))
        conditions[1].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkRight2.png"),(20, 20)))
        conditions.append([])
        conditions[2].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkDown1.png"),(20, 20)))
        conditions[2].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkDown2.png"),(20, 20)))
        conditions.append([])
        conditions[3].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkLeft1.png"),(20, 20)))
        conditions[3].append(pygame.transform.scale(pygame.image.load("./Entity/Ghost/ghostPinkLeft2.png"),(20, 20)))
        return conditions
        
    def genPacmanImg(self):
        conditions = list()
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

    def genGameOverImg(self):
        conditions = list()
        for i in range(10):
            conditions.append(pygame.transform.scale(pygame.image.load("./Entity/GameOver/GameOver" + str(i + 1) + ".png"),
                                        (248, 148)))
        return conditions



    def set_menu(self):
        pygame.mixer.Sound('./SoundsEffect/pacman_intermission.wav').play()
        self.state = STATES["menu"]
        self.objects.clear()
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
        self.counterOfEatenFruits = 0
        self.gameover_exists = False
        self.counter = Counter()
        self.state = STATES["game"]
        self.objects.clear()
        self.objects.append(GameField([pygame.transform.scale(pygame.image.load("./Entity/Map.png"),
                                        (424, 468))], [0, 0, 424, 468]))
        self.objects.append(Pacman(self.genPacmanImg(), [229, 255, 20, 20], 0, 1))
        self.start_v = 33
        self.finish_v = 34
        cnt = -1
        for v in self.graph.coordinates:
            cnt += 1
            name_on = "./Entity/Fruit/ SeedOn.png"
            name_off = "./Entity/Fruit/seedOff.png"
            self.objects.append(Seed([[pygame.transform.scale(pygame.image.load(name_on), (2, 2))],
                                     [pygame.transform.scale(pygame.image.load(name_off), (2, 2))]],
                                     [v[0] - 1, v[1] - 1, 2, 2]))                   ## 3-68 элементы - зерна  
            if 28 <= cnt <= 30:
                self.objects[-1].change_type(1)
        self.objects.append(Ghost(self.genPinkGhostImg(), [self.graph.coordinates[29][0], self.graph.coordinates[29][1], 20, 20], 0)) ## 69 элемент - розовый призрак

        cnt = -1
        cnt = random.randint(0, 66)    # генерация фруктов
        while (28 <= cnt <= 30):
                cnt = random.randint(0, 66)
        v = self.graph.coordinates[cnt]
        self.objects[cnt + 2].change_type(1)
        i = random.randint(1, 5)
        self.fruit_index = len(self.objects)
        name_on = "./Entity/Fruit/fruit" + str(i) + ".png"
        name_off = "./Entity/Fruit/seedOff.png"
        self.objects.append(Fruit([[pygame.transform.scale(pygame.image.load(name_on), (15, 15))],
                                 [pygame.transform.scale(pygame.image.load(name_off), (15, 15))]],
                                 [v[0] - 5, v[1] - 8, 15, 15]))
        #self.objects[69].move_to_point([self.graph.coordinates[29][0], self.graph.coordinates[29][1]])
        self.objects[69].start_moving_to_point([self.graph.coordinates[23][0], self.graph.coordinates[23][1]])

    def finish_game(self):
        if self.counterOfEatenFruits == 63:  # 63
            return True
        else:
            return False

    def set_settings(self):
        self.state = STATES["settings"]
        self.objects.clear()

    def set_exit(self):
        self.immediately_close = True

    def loop(self):
        self.screen.fill((0, 0, 0))
        for object in self.objects:
            object.draw(self.screen)
        #if self.state == STATES["game"]:
            # for v in self.graph.coordinates:                     ##Рисует вершины графа для проверки
            #      pygame.draw.circle(self.screen, (0, 255, 0), v, 1)
        if self.state == STATES["game"]:
            self.counter.draw(self.screen)
        pygame.display.flip()

    def game_logic(self):
        if (self.finish_game()):
            if not self.gameover_exists:
                self.objects.append(GameOver(self.genGameOverImg(), [88, 150, 448, 248], 0))
                self.gameover_exists = True
        else:
            if self.state == STATES["game"]:
                self.eat_seed()
                self.check_finish()
                self.objects[1].move_to_point()
                self.objects[1].move()
                self.objects[69].move_to_point()

    def next_state(self):
        if self.state == STATES["game"]:
            for el in self.objects:
                el.next_state()

    def eat_seed(self):
        if self.state == STATES["game"]:
            if not(self.objects[self.fruit_index].getType()):
                rect = self.objects[self.fruit_index].getRect()
                if self.objects[1].collide_with([rect[0] + rect[2] // 2, rect[1] + rect[3] // 2]):
                    self.objects[self.fruit_index].change_type(1)
                    self.counter.updatePoints(100)
                    pygame.mixer.Sound('./SoundsEffect/pacman_eatfruit.wav').play()

            if not(self.objects[self.finish_v + 2].getType()):
                if self.objects[1].collide_with(self.graph.coordinates[self.finish_v]):
                    self.objects[self.finish_v + 2].change_type(1)
                    self.counter.updatePoints(10)
                    pygame.mixer.Sound('./SoundsEffect/pacman_chomp.wav').play()
                    self.counterOfEatenFruits += 1

    def check_finish(self):
        if self.objects[1].collide_with(self.graph.coordinates[self.finish_v]):
            self.in_finish = True
            from_coord = self.graph.coordinates[self.finish_v]
            adjVertex = self.graph.adjVertex[self.finish_v]
            self.turn_right = self.turn_left = self.turn_down = self.turn_up = False
            for v_num in adjVertex:
                v = self.graph.coordinates[v_num]
                move_vector = [v[0] - from_coord[0], v[1] - from_coord[1]]
                if -3 <= move_vector[0] <= 3:
                    move_vector[0] = 0
                if -3 <= move_vector[1] <= 3:
                    move_vector[1] = 0
                if move_vector[0] > 0:
                    self.turn_right = True
                if move_vector[0] < 0:
                    self.turn_left = True
                if move_vector[1] > 0:
                    self.turn_down = True
                if move_vector[1] < 0:
                    self.turn_up = True
            pacman_type = self.objects[1].get_type()
            if pacman_type == 0 and not self.turn_up:
                self.objects[1].stop()
            if pacman_type == 1 and not self.turn_right:
                self.objects[1].stop()
            if pacman_type == 2 and not self.turn_down:
                self.objects[1].stop()
            if pacman_type == 3 and not self.turn_left:
                self.objects[1].stop()
            if pacman_type == 0 and self.turn_up:
                self.objects[1].start_moving()
            if pacman_type == 1 and self.turn_right:
                self.objects[1].start_moving()
            if pacman_type == 2 and self.turn_down:
                self.objects[1].start_moving()
            if pacman_type == 3 and self.turn_left:
                self.objects[1].start_moving()

        else:
            if self.in_finish:
                self.in_finish = False
                self.choose_next_target()
            from_coord = self.graph.coordinates[self.start_v]
            to_coord = self.graph.coordinates[self.finish_v]
            self.turn_right = self.turn_left = self.turn_down = self.turn_up = False
            move_vector = [to_coord[0] - from_coord[0], to_coord[1] - from_coord[1]]
            if move_vector[0] > 0:
                self.turn_right = True
                self.turn_left = True
            if move_vector[0] < 0:
                self.turn_left = True
                self.turn_right = True
            if move_vector[1] > 0:
                self.turn_down = True
                self.turn_up = True
            if move_vector[1] < 0:
                self.turn_down = True
                self.turn_up = True

    def choose_next_target(self):
        self.start_v = self.finish_v
        from_coord = self.graph.coordinates[self.start_v]
        for v_num in self.graph.adjVertex[self.start_v]:
            v = self.graph.coordinates[v_num]
            move_vector = [v[0] - from_coord[0], v[1] - from_coord[1]]
            if move_vector[0] > 0 and self.objects[1].get_type() == 1:
                self.finish_v = v_num
            if move_vector[0] < 0 and self.objects[1].get_type() == 3:
                self.finish_v = v_num
            if move_vector[1] > 0 and self.objects[1].get_type() == 2:
                self.finish_v = v_num
            if move_vector[1] < 0 and self.objects[1].get_type() == 0:
                self.finish_v = v_num
