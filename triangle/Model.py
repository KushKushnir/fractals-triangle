import pygame

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
