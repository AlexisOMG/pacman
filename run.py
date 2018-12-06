from game import game
import pygame

def main():
    SIZE = 424, 518
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    gm = game(screen, SIZE)
    while not gm.immediately_close:
        gm.process_events(pygame.event.get())
        gm.loop()
        gm.game_logic()

if __name__ == "__main__":
    main()
