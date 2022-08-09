import pygame

class Controller():
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self.printMsg()

	def printMsg(self):
		print("Controller init")

	#CANT MAKE RESISABLE RN, FIX IF POSSIBLE
	def run(self, draw_button, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		while self.model.end_game == 0:
			for event in pygame.event.get():
				mouse_pos = pygame.mouse.get_pos()
				if event.type == pygame.VIDEORESIZE:
					screen_width, screen_height = pygame.VIDEORESIZE
				if event.type == pygame.QUIT:
					raise SystemExit
				if event.type == pygame.MOUSEBUTTONDOWN:
					if draw_button.is_over(mouse_pos):
						self.model.draw_line()
						self.view.redraw(screen, SCREEN_WIDTH, SCREEN_HEIGHT, draw_button)
						pygame.display.update()






