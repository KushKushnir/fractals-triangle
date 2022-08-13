import pygame

class Triangle():
	def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.right = [SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6, 
			SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6]
		self.left = [SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 1/6, 
			SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6]
		self.bot = [SCREEN_WIDTH * 1/6, SCREEN_HEIGHT * 5/6, 
			SCREEN_WIDTH * 5/6, SCREEN_HEIGHT * 5/6]

class Model():
	end_game = 0
	num_triangles = 0
	og_tri = 0

	def __init__(self):
		self.printMsg()
		#arr[x1, y1, x2, y2]		

	def printMsg(self):
		print("Model init")

	def draw_og_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		#if self.num_triangles == 0:
		self.num_triangles += 1
		self.og_tri = Triangle(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
		#Draw left
		pygame.draw.line(screen, "black", 
			(self.og_tri.left[0], self.og_tri.left[1]), 
			(self.og_tri.left[2], self.og_tri.left[3]), 3)
		#draw right
		pygame.draw.line(screen, "black", 
			(self.og_tri.right[0], self.og_tri.right[1]), 
			(self.og_tri.right[2], self.og_tri.right[3]), 3)
		#draw bot
		pygame.draw.line(screen, "black", 
			(self.og_tri.bot[0], self.og_tri.bot[1]), 
			(self.og_tri.bot[2], self.og_tri.bot[3]), 3)
		
		if self.num_triangles > 1:
			#if self.num_triangles % 2 == 0:		
			#	self.draw_left_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
			#self.draw_right_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)			
			self.draw_up_tri(screen, SCREEN_WIDTH, SCREEN_HEIGHT)			
			
		print(self.num_triangles)
		
	def draw_up_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		for i in range(self.num_triangles - 1):
				self.og_tri.bot = [
					self.midpoint(self.og_tri.left[0], self.og_tri.left[2]),
					self.midpoint(self.og_tri.left[3], self.og_tri.left[1]),
					self.og_tri.left[0] - (self.midpoint(self.og_tri.left[0], self.og_tri.left[2]) + self.og_tri.left[0]),
					self.midpoint(self.og_tri.left[3], self.og_tri.left[1])]
					

	def draw_left_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		#self.num_triangles += 1
		for i in range(self.num_triangles - 1):
			self.og_tri.bot = [
				self.midpoint(self.og_tri.right[2], self.og_tri.right[0]),
				self.midpoint(self.og_tri.right[3], self.og_tri.right[1]),
				self.og_tri.right[0] - (self.midpoint(self.og_tri.right[2], self.og_tri.right[0]) - self.og_tri.right[0]),
				self.midpoint(self.og_tri.right[3], self.og_tri.right[1])]

			self.og_tri.right = [
				self.og_tri.bot[2],
				self.og_tri.bot[3],
				self.og_tri.right[0],
				self.og_tri.right[3]]

			self.og_tri.left = [
				self.og_tri.bot[0],
				self.og_tri.bot[1],
				self.og_tri.right[2],
				self.og_tri.right[3]]

			#Draw bot
			pygame.draw.line(screen, "black",
				(self.og_tri.bot[2], self.og_tri.bot[3]),# x2, y2
				(self.og_tri.bot[0], self.og_tri.bot[1]), 3)#x1, y1

			#Draw Right
			pygame.draw.line(screen, "black",
				(self.og_tri.right[2], self.og_tri.right[3]),# x2, y2
				(self.og_tri.right[0], self.og_tri.right[1]), 3)#x1, y1

			#Draw left(mirrored to right now)
			pygame.draw.line(screen, "black",
				(self.og_tri.left[2], self.og_tri.left[3]),# x2, y2
				(self.og_tri.left[0], self.og_tri.left[1]), 3)#x1, y1

	def draw_right_tri(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		#self.num_triangles += 1
		for i in range(self.num_triangles - 1):
			self.og_tri.bot = [
				self.midpoint(self.og_tri.left[0], self.og_tri.left[2]),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1]),
				self.og_tri.left[0] - (self.midpoint(self.og_tri.left[0], self.og_tri.left[2]) + self.og_tri.left[0]),
				self.midpoint(self.og_tri.left[3], self.og_tri.left[1])]

			self.og_tri.left = [
				self.og_tri.bot[2],
				self.og_tri.bot[3],
				self.og_tri.left[0],
				self.og_tri.left[3]]

			self.og_tri.right = [
				self.og_tri.bot[0],
				self.og_tri.bot[1],
				self.og_tri.left[2],
				self.og_tri.left[3]]

			#Draw bot
			pygame.draw.line(screen, "black",
				(self.og_tri.bot[2], self.og_tri.bot[3]),# x2, y2
				(self.og_tri.bot[0], self.og_tri.bot[1]), 3)#x1, y1

			#Draw left(mirrored to right now)
			pygame.draw.line(screen, "black",
				(self.og_tri.left[2], self.og_tri.left[3]),# x2, y2
				(self.og_tri.left[0], self.og_tri.left[1]), 3)#x1, y1

			#Draw Right
			pygame.draw.line(screen, "black",
				(self.og_tri.right[2], self.og_tri.right[3]),# x2, y2
				(self.og_tri.right[0], self.og_tri.right[1]), 3)#x1, y1

		pygame.display.flip()

	def midpoint(self, z1, z2):
		return ((z1 - z2) //2) + z2
			

			


