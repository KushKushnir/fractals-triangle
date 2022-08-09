import pygame

class View():
	def __init__(self, model):
		self.printMsg()

	def printMsg(self):
		print("View init")

	def redraw(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, draw_button):
		screen.fill((214, 169, 105))
		draw_button.draw(screen, "black")
		pygame.display.flip()





