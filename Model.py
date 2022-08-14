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
	og_tri = 0

	def __init__(self):
		self.printMsg()	

	def printMsg(self):
		print("Model init")

	def draw_og_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.num_triangles += 1
		self.og_tri = Triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
		self.draw_triangles(screen, 
			SCREEN_WIDTH, SCREEN_HEIGHT, 1)
		if self.num_triangles > 1:
			self.og_tri.bot = [
				self.og_tri.left[2] + (self.og_tri.left[2] - 
					self.midpoint(self.og_tri.left[0], self.og_tri.left[2])),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1]),
				self.midpoint(self.og_tri.left[0], self.og_tri.left[2]),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1])]

			self.og_tri.left = [
				self.og_tri.left[2],
				self.og_tri.left[1],
				self.og_tri.bot[0],
				self.og_tri.bot[1]]

			self.og_tri.right = [
				self.og_tri.left[0],
				self.og_tri.left[1],
				self.og_tri.bot[2],
				self.og_tri.bot[3]]
			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 2)

	
	def set_up_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i in range(3, self.num_triangles + 1):
			print("num = ", self.num_triangles)
			print("i = ", i)
			self.og_tri.bot = [
				self.midpoint(self.og_tri.left[0],self.og_tri.left[2]),#x2
					self.og_tri.left[3] - 
					(self.midpoint(self.og_tri.left[1], self.og_tri.left[3])
					- self.og_tri.left[3]),#y2
				self.midpoint(self.og_tri.right[0],self.og_tri.right[2]),#x2
				self.og_tri.right[3] - 
					(self.midpoint(self.og_tri.right[1], self.og_tri.right[3])
					- self.og_tri.right[3])]#y2

			self.og_tri.right = [
				self.midpoint(self.og_tri.bot[2], self.og_tri.bot[0]),
				self.og_tri.left[3], 
				self.og_tri.bot[2],
				self.og_tri.bot[3]]

			self.og_tri.left = [
				self.midpoint(self.og_tri.bot[2], self.og_tri.bot[0]), 
				self.og_tri.left[3], 
				self.og_tri.bot[0], 
				self.og_tri.bot[1]]

			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, i)


	def set_left_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i in range(3, self.num_triangles + 1):
			self.og_tri.bot = [
				self.midpoint(self.og_tri.right[2], self.og_tri.right[0]),
				self.midpoint(self.og_tri.right[3], self.og_tri.right[1]),
				self.og_tri.right[2] - 
					(self.midpoint(self.og_tri.right[2], self.og_tri.right[0])
					- self.og_tri.right[2]),
				self.midpoint(self.og_tri.right[3], self.og_tri.right[1])]

			self.og_tri.left = [
				self.og_tri.right[2],
				self.og_tri.right[1],
				self.og_tri.bot[0],
				self.og_tri.bot[1]]

			self.og_tri.right = [
				self.og_tri.right[2],
				self.og_tri.right[1],
				self.og_tri.bot[2],
				self.og_tri.bot[3]]
			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, i)


	def set_right_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i in range(3, self.num_triangles + 1):
			self.og_tri.bot = [
				self.og_tri.left[2] + (self.og_tri.left[2] - 
					self.midpoint(self.og_tri.left[2], self.og_tri.left[0])),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1]),
				self.midpoint(self.og_tri.left[2], self.og_tri.left[0]),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1])]

			self.og_tri.right = [
				self.og_tri.left[2],
				self.og_tri.left[1],
				self.og_tri.bot[2],
				self.og_tri.bot[3]]

			self.og_tri.left = [
				self.og_tri.left[2],
				self.og_tri.left[1],
				self.og_tri.bot[0],
				self.og_tri.bot[1]]
			self.draw_triangles(screen, SCREEN_WIDTH, SCREEN_HEIGHT, i)


	def midpoint(self, z1, z2):
		return ((z1 - z2) //2) + z2

	def draw_triangles(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, i):		
		if i == self.num_triangles:
			#draw bot
			pygame.draw.line(screen, "red", 
				(self.og_tri.bot[2], self.og_tri.bot[3]),# x2, y2
				(self.og_tri.bot[0], self.og_tri.bot[1]), 3)# x1, y1
			#Draw left
			pygame.draw.line(screen, "red",
				(self.og_tri.left[2], self.og_tri.left[3]),# x2, y2
				(self.og_tri.left[0], self.og_tri.left[1]), 3)# x1, y1
			#draw right
			pygame.draw.line(screen, "red", 
				(self.og_tri.right[2], self.og_tri.right[3]),# x2, y2
				(self.og_tri.right[0], self.og_tri.right[1]), 3)# x1, y1
		else:
			#draw bot
			pygame.draw.line(screen, "black", 
				(self.og_tri.bot[2], self.og_tri.bot[3]),# x2, y2
				(self.og_tri.bot[0], self.og_tri.bot[1]), 3)# x1, y1
			#Draw left
			pygame.draw.line(screen, "black",
				(self.og_tri.left[2], self.og_tri.left[3]),# x2, y2
				(self.og_tri.left[0], self.og_tri.left[1]), 3)# x1, y1
			#draw right
			pygame.draw.line(screen, "black", 
				(self.og_tri.right[2], self.og_tri.right[3]),# x2, y2
				(self.og_tri.right[0], self.og_tri.right[1]), 3)# x1, y1


