import pygame

class View():
	def __init__(self, model):
		self.printMsg()

	def printMsg(self):
		print("View init")

	def redraw(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, 
		right_triangle_button, up_triangle_button, 
		left_triangle_button, reset_button):

		screen.fill(("#191970"))
		right_triangle_button.draw(screen, "black")
		up_triangle_button.draw(screen, "black")
		left_triangle_button.draw(screen, "black")
		left_triangle_button.draw(screen, "black")
		reset_button.draw(screen, "black")
		pygame.display.flip()





