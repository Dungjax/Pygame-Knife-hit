from pygame import init,display
init()
from setting import *
from circle import Circle
class Game:
	def __init__(self):
		self.circle=Circle("wood0.png")
		circle_group.add(self.circle)
	def draw(self):
		circle_group.draw(screen)
	def update(self):
		 circle_group.update()
	def loop(self):
		#loop
		while 1:
			screen.blit(bg,(0,0))
			self.draw()
			self.update()
			display.update()
game=Game()
game.loop()