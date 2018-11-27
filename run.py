from game import game

def main():
    SIZE = 424, 468
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    gm = game(screen, SIZE)
    while not gm.immediately_close:
        gm.process_events(pygame.event.get())
        gm.loop()

if __name__ == "__main__":
    main()

