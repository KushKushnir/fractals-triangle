import pygame

class Triangle():
	def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.right = [SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6]#x1, y1

		self.left = [SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6]#x1, y1

		self.bot = [SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6,#x2, y2
		SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6]#x1, y1

class Model():
	end_game = 0
	num_triangles = 0
	original_triangle = 0
	arr = []

	def __init__(self):
		self.printMsg()	

	def printMsg(self):
		print("Model init")

	#IN MODEL
	def set_second_triangle(self):
		self.original_triangle.bot = [
			self.original_triangle.left[2] + (self.original_triangle.left[2] - 
			self.midpoint(self.original_triangle.left[0], self.original_triangle.left[2])),
			self.midpoint(self.original_triangle.left[3], self.original_triangle.left[1]),
			self.midpoint(self.original_triangle.left[0], self.original_triangle.left[2]),
			self.midpoint(self.original_triangle.left[3], self.original_triangle.left[1])]
			
		self.original_triangle.left = [
			self.original_triangle.left[2],
			self.original_triangle.left[1],
			self.original_triangle.bot[0],
			self.original_triangle.bot[1]]

		self.original_triangle.right = [
			self.original_triangle.left[0],
			self.original_triangle.left[1],
			self.original_triangle.bot[2],
			self.original_triangle.bot[3]]


	#IN MODEL
	def add_up(self):
		self.arr.append("^")
	#IN MODEL
	def add_left(self):
		self.arr.append("<")
	#IN MODEL
	def add_right(self):
		self.arr.append(">")

	#IN MODEL
	def set_up_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.original_triangle.bot = [
			self.midpoint(self.original_triangle.left[0],self.original_triangle.left[2]),#x2
				self.original_triangle.left[3] - 
				(self.midpoint(self.original_triangle.left[1], self.original_triangle.left[3])
				- self.original_triangle.left[3]),#y2
			self.midpoint(self.original_triangle.right[0],self.original_triangle.right[2]),#x2
			self.original_triangle.right[3] - 
				(self.midpoint(self.original_triangle.right[1], self.original_triangle.right[3])
				- self.original_triangle.right[3])]#y2

		self.original_triangle.right = [
			self.midpoint(self.original_triangle.bot[2], self.original_triangle.bot[0]),
			self.original_triangle.left[3], 
			self.original_triangle.bot[2],
			self.original_triangle.bot[3]]

		self.original_triangle.left = [
			self.midpoint(self.original_triangle.bot[2], self.original_triangle.bot[0]), 
			self.original_triangle.left[3], 
			self.original_triangle.bot[0], 
			self.original_triangle.bot[1]]

	#IN MODEL
	def set_left_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.original_triangle.bot = [
			self.midpoint(self.original_triangle.right[2], self.original_triangle.right[0]),
			self.midpoint(self.original_triangle.right[3], self.original_triangle.right[1]),
			self.original_triangle.right[2] - 
				(self.midpoint(self.original_triangle.right[2], self.original_triangle.right[0])
				- self.original_triangle.right[2]),
			self.midpoint(self.original_triangle.right[3], self.original_triangle.right[1])]

		self.original_triangle.left = [
			self.original_triangle.right[2],
			self.original_triangle.right[1],
			self.original_triangle.bot[0],
			self.original_triangle.bot[1]]

		self.original_triangle.right = [
			self.original_triangle.right[2],
			self.original_triangle.right[1],
			self.original_triangle.bot[2],
			self.original_triangle.bot[3]]

	#IN MODEL
	def set_right_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.original_triangle.bot = [
			self.original_triangle.left[2] + (self.original_triangle.left[2] - 
				self.midpoint(self.original_triangle.left[2], self.original_triangle.left[0])),
			self.midpoint(self.original_triangle.left[3], self.original_triangle.left[1]),
			self.midpoint(self.original_triangle.left[2], self.original_triangle.left[0]),
			self.midpoint(self.original_triangle.left[3], self.original_triangle.left[1])]

		self.original_triangle.right = [
			self.original_triangle.left[2],
			self.original_triangle.left[1],
			self.original_triangle.bot[2],
			self.original_triangle.bot[3]]

		self.original_triangle.left = [
			self.original_triangle.left[2],
			self.original_triangle.left[1],
			self.original_triangle.bot[0],
			self.original_triangle.bot[1]]

	#IN MODEL
	def reset(self):
		self.num_triangles = 0
		self.arr.clear()

	#IN MODEL
	def midpoint(self, z1, z2):
		return ((z1 - z2) //2) + z2

	#In VIEW
	def set_all(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i, n in enumerate(self.arr[2:]):
			#print(self.num_triangles)
			#print("i = ",i, " n = ", n)
			if n == "^":
				self.set_up_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			elif n == ">":
				self.set_right_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			elif n == "<":
				self.set_left_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			else:
				print("ERROR")
			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, i)


	#IN VIEW
	def draw_original_triangle(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		pygame.draw.line(screen, "white", 
			(self.original_triangle.bot[2], self.original_triangle.bot[3]),# x2, y2
			(self.original_triangle.bot[0], self.original_triangle.bot[1]), 3)# x1, y1
		#Draw left
		pygame.draw.line(screen, "white",
			(self.original_triangle.left[2], self.original_triangle.left[3]),# x2, y2
			(self.original_triangle.left[0], self.original_triangle.left[1]), 3)# x1, y1
		#draw right
		pygame.draw.line(screen, "white", 
			(self.original_triangle.right[2], self.original_triangle.right[3]),# x2, y2
			(self.original_triangle.right[0], self.original_triangle.right[1]), 3)# x1, y1
	
	#IN VIEW
	def draw_triangles(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, i):
		self.draw_original_triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
		if i == self.num_triangles - 3 and self.num_triangles >= 3:
			#draw bot
			pygame.draw.line(screen, "red", 
				(self.original_triangle.bot[2], self.original_triangle.bot[3]),# x2, y2
				(self.original_triangle.bot[0], self.original_triangle.bot[1]), 3)# x1, y1
			#Draw left
			pygame.draw.line(screen, "red",
				(self.original_triangle.left[2], self.original_triangle.left[3]),# x2, y2
				(self.original_triangle.left[0], self.original_triangle.left[1]), 3)# x1, y1
			#draw right
			pygame.draw.line(screen, "red", 
				(self.original_triangle.right[2], self.original_triangle.right[3]),# x2, y2
				(self.original_triangle.right[0], self.original_triangle.right[1]), 3)# x1, y1

	#IN VIEW
	def set_original_triangle(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.num_triangles += 1
		self.original_triangle = Triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

		self.draw_original_triangle(screen,SCREEN_WIDTH, SCREEN_HEIGHT)

		if self.num_triangles > 1:
			self.set_second_triangle()
			self.draw_original_triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)




