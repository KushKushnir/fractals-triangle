import pygame

class Triangle():
	def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.right = [SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6]#x1, y1

		self.left = [SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6]#x1, y1

		self.bot = [SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6]#x1, y1

class View():
	def __init__(self, model):
		self.model = model
		self.printMsg()

	def printMsg(self):
		print("View init")

	def redraw(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, 
		right_triangle_button, up_triangle_button, 
		left_triangle_button, reset_button):

		screen.fill("#191970")
		right_triangle_button.draw(screen, "black")
		up_triangle_button.draw(screen, "black")
		left_triangle_button.draw(screen, "black")
		reset_button.draw(screen, "black")
		pygame.display.flip()

		#In VIEW
	def set_all(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i, n in enumerate(self.model.arr[2:]):
			#print(self.num_triangles)
			#print("i = ",i, " n = ", n)
			if n == "^":
				self.model.set_up_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			elif n == ">":
				self.model.set_right_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			elif n == "<":
				self.model.set_left_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			else:
				print("ERROR")
			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, i)


	# #IN VIEW
	def draw_original_triangle(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		pygame.draw.line(screen, "white", 
			(self.model.original_triangle.bot[2], self.model.original_triangle.bot[3]),# x2, y2
			(self.model.original_triangle.bot[0], self.model.original_triangle.bot[1]), 3)# x1, y1
		#Draw left
		pygame.draw.line(screen, "white",
			(self.model.original_triangle.left[2], self.model.original_triangle.left[3]),# x2, y2
			(self.model.original_triangle.left[0], self.model.original_triangle.left[1]), 3)# x1, y1
		#draw right
		pygame.draw.line(screen, "white", 
			(self.model.original_triangle.right[2], self.model.original_triangle.right[3]),# x2, y2
			(self.model.original_triangle.right[0], self.model.original_triangle.right[1]), 3)# x1, y1
	
	# #IN VIEW
	def draw_triangles(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, i):
		self.draw_original_triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
		if i == self.model.num_triangles - 3 and self.model.num_triangles >= 3:
			#draw bot
			pygame.draw.line(screen, "red", 
				(self.model.original_triangle.bot[2], self.model.original_triangle.bot[3]),# x2, y2
				(self.model.original_triangle.bot[0], self.model.original_triangle.bot[1]), 3)# x1, y1
			#Draw left
			pygame.draw.line(screen, "red",
				(self.model.original_triangle.left[2], self.model.original_triangle.left[3]),# x2, y2
				(self.model.original_triangle.left[0], self.model.original_triangle.left[1]), 3)# x1, y1
			#draw right
			pygame.draw.line(screen, "red", 
				(self.model.original_triangle.right[2], self.model.original_triangle.right[3]),# x2, y2
				(self.model.original_triangle.right[0], self.model.original_triangle.right[1]), 3)# x1, y1

	# #IN VIEW
	def set_original_triangle(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.model.num_triangles += 1
		self.model.original_triangle = Triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

		self.draw_original_triangle(screen,SCREEN_WIDTH, SCREEN_HEIGHT)

		if self.model.num_triangles > 1:
			self.model.set_second_triangle()
			self.draw_original_triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)



