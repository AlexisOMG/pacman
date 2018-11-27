import pygame

class game():
	def __init__(self, screen, screen_size):
		self.screen = screen
		self.screen_size = screen_size
		self.objects = []
		self.immediately_close = False

	def process_events(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				self.immediately_close = True
			for object in self.objects:
				object.check_event(event)

	def loop(self):
		self.screen.fill((0, 0, 0))
		for object in self.objects:
			object.draw(self.screen)
		pygame.display.flip()

	def game_logic(self):
		pass
