from pygame import display,image,sprite,fastevent
#setup screen
Width=1080
Height=2290
H_Width=Width/2
Hp5_Height=Height/2.5
screen=display.set_mode((Width,Height))
#color
bright_blue=(100,200,250)
#image
bg=image.load("bg.png").convert()
#sprite group
circle_group=sprite.Group()
knife_group=sprite.Group()
#event
fastevent.init()