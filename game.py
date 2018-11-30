import pygame
from constants import STATES, GAMEPLAY_STATES
from button import Button

class game():
	def __init__(self, screen, screen_size):
		self.screen = screen
		self.screen_size = screen_size
		self.objects = []
		self.immediately_close = False
		self.state = STATES["menu"]
		self.game_state = GAMEPLAY_STATES["level_1"]
		self.set_menu()

	def process_events(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				self.immediately_close = True
			for object in self.objects:
				object.check_event(event)

	def set_menu(self):
		self.objects = []
		self.objects.append(Button([pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonNotPressed.png"), (100, 25)),
									pygame.transform.scale(pygame.image.load("./Entity/Buttons/ButtonPreesed.png"), (100, 25))],
								   [self.screen_size[0] // 2 - 50, self.screen_size[1] / 2 - 60, 100, 25], self.set_game))

	def set_game(self):
		self.objects = []

	def loop(self):
		self.screen.fill((0, 0, 0))
		for object in self.objects:
			object.draw(self.screen)
		pygame.display.flip()

	def game_logic(self):
		pass
