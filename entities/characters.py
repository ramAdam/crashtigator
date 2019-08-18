from pyglet.window import key
from pyglet.sprite import Sprite
from loader.animations import nick

class Hero(Sprite):
	def __init__(self, *args, **kwargs):
		self.default = Sprite(nick.get('idle')).image
		super().__init__(img=self.default, **kwargs)
		self.walk = Sprite(nick.get('walk'))
		self.shoot = Sprite(nick.get('shoot'))
		self.keys = dict(up=False, down=False, right=False, left=False, shoot=False)
		self.speed = 100

	def on_key_press(self, symbol, modifiers):

		if symbol == key.RIGHT:
			self.keys['right'] = True
			self.image = self.walk.image
		elif symbol == key.S:
		    self.image = self.shoot.image
		    
	def on_key_release(self, symbol, modifiers):
			self.image = self.default
			self.keys['right'] = False

	def update(self, dt):
		# if self.keys['right']:
		# 	self.x += self.speed * dt
		pass
		
		




		



