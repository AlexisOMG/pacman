from game import game
import pygame
import time

def main():
    SIZE = 424, 518
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    gm = game(screen, SIZE)
    cur_time = time.time()
    while not gm.immediately_close:
        gm.process_events(pygame.event.get())
        if time.time() - cur_time > 0.1:
            gm.next_state()
            cur_time = time.time()
        gm.loop()
        gm.game_logic()

if __name__ == "__main__":
    main()
