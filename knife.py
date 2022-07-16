from pygame import sprite,image,transform
from setting import H_Width,Hp5_Height
from math import sin,cos,radians
class Knife(sprite.Sprite):
		def __init__(self):
			super().__init__()
			self.image=image.load("k0.png").convert_alpha()
			self.image_t=self.image
			self.rect=self.image.get_rect()
			self.rect.center=H_Width,1600
			self.angle=0
			self.is_throw=0
			self.is_hit=0
			self.speed=10
					
		def hit(self):
			distance=self.rect.centery-(Hp5_Height)
			if distance<self.image.get_height():
				self.is_hit=1
			if self.is_hit!=1:
				self.speed+=20
				self.rect.centery-=self.speed
		def rotate(self):
				self.image=transform.rotate(self.image_t,self.angle)
				circle_half_size=200
				knife_half_width=22.5
				knife_half_height=117.5
				
				self.rect.centerx=H_Width+circle_half_size*sin(radians(self.angle))-self.image.get_width()/2+knife_half_width
				
				self.rect.centery=Hp5_Height+circle_half_size*cos(radians(self.angle))-self.image.get_height()/2+knife_half_height
				
		def update(self):
			if self.is_hit==1:
				self.rotate()
				self.angle+=3
			self.hit()