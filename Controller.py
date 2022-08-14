import pygame

class Controller():
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self.printMsg()

	def printMsg(self):
		print("Controller init")

	#CANT MAKE RESISABLE RN, FIX IF POSSIBLE
	def run(self, 
		right_triangle_button, up_triangle_button, left_triangle_button, 
		screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		while self.model.end_game == 0:
			for event in pygame.event.get():
				mouse_pos = pygame.mouse.get_pos()
				if event.type == pygame.VIDEORESIZE:
					screen_width, screen_height = pygame.VIDEORESIZE
				if event.type == pygame.QUIT:
					raise SystemExit
				if event.type == pygame.MOUSEBUTTONDOWN:
					#If user clicks buttons
					if right_triangle_button.is_over(mouse_pos):
						self.view.redraw(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
							right_triangle_button, up_triangle_button, left_triangle_button)
						self.model.draw_og_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						self.model.set_right_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						pygame.display.update()
					if up_triangle_button.is_over(mouse_pos):
						self.view.redraw(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
							right_triangle_button, up_triangle_button, left_triangle_button)
						self.model.draw_og_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						self.model.set_up_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						pygame.display.update()
					if left_triangle_button.is_over(mouse_pos):
						self.view.redraw(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 
							right_triangle_button, up_triangle_button, left_triangle_button)
						self.model.draw_og_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						self.model.set_left_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
						pygame.display.update()






