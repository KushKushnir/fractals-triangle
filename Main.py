import pygame
import Model as m
import View as v
import Controller as c

class Button():
	def __init__(self, colour, x, y, button_width, button_height, text):
		self.colour = colour
		self.x = x
		self.y = y
		self.button_width = button_width
		self.button_height = button_height
		self.text = text

	def draw(self, screen, outline_colour):
		pygame.draw.rect(screen, outline_colour, (self.x-2, self.y-2, self.button_width+4, self.button_height+4),0)
		pygame.draw.rect(screen, self.colour, (self.x,self.y,self.button_width, self.button_height),0)
		font = pygame.font.SysFont("merriweather", 30)
		text = font.render(self.text, 1, (0,0,0))
		screen.blit(text, (self.x + (self.button_width/2 - text.get_width()/2), self.y + (self.button_height/2 - text.get_height()/2)))

	#Function to tell us if mouse position is over button
	def is_over(self, pos):
		#pos is the mouse position
		if pos[0] > self.x and pos[0] < self.x + self.button_width:
			if pos[1] > self.y and pos[1] < self.y + self.button_height:
				return True
			return False

class Main():
	def __init__(self):
		SCREEN_WIDTH = 900
		SCREEN_HEIGHT = 650
		before_game = 0
		pygame.font.init()
		pygame.display.init()
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
		screen.fill((100,100,100))
		caption = "Fractals"
		pygame.display.set_caption(caption)
		pygame.display.flip()

		#Run up Start Screen
		while before_game == 0:
			for event in pygame.event.get():
				if event.type == pygame.VIDEORESIZE:
					self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.size
				if event.type == pygame.QUIT:
					raise SystemExit
				if event.type == pygame.MOUSEBUTTONDOWN:
					before_game = 1
					self.start(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
					pygame.display.flip()

	def start(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
		model = m.Model()
		view = v.View(model)
		controller = c.Controller(model, view)

		#set up buttons here
		draw_button = Button("#4ecbc4", SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5, 100, 100, "Draw")
		view.redraw(screen, SCREEN_WIDTH, SCREEN_HEIGHT, draw_button)
		controller.run(draw_button, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

#SET FRACTALS
#EXCEPTIONS
#TEST DRIVEN DEVELOPMENT

#PEP8
#MVC
start = Main()



