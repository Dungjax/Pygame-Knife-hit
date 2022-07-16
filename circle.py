from pygame import sprite,image,transform
from setting import H_Width,Hp5_Height
class Circle(sprite.Sprite):
			def __init__(self,img_name):
				super().__init__()
				self.image=image.load(img_name).convert_alpha()
				self.image_t=self.image
				self.rect=self.image.get_rect()
				self.rect.center=H_Width,Hp5_Height
				self.angle=0
				
			def rotate(self):
				self.image=transform.rotate(self.image_t,self.angle)
				
				circle_half_size=200
				self.rect.centerx=H_Width+circle_half_size-self.image.get_width()/2
				self.rect.centery=Hp5_Height+circle_half_size-self.image.get_height()/2
				
			
			def update(self):
				self.angle+=3
				self.rotate()
				