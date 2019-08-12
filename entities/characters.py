from pyglet.window import key
from pyglet.sprite import Sprite
from loader.animations import nick

class Hero(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = self.image
        self.walk = Sprite(nick.get('walk'), x=20)
        self.shoot = Sprite(nick.get('shoot'), x=20)
        self.key_pressed = []

    def on_key_press(self, symbol, modifiers):
      	
        if symbol == key.RIGHT:
            self.image = self.walk.image
            self.key_pressed.append(symbol)
        elif symbol == key.S:
            self.image = self.shoot.image
            self.key_pressed.append(symbol)
            
    def on_key_release(self, symbol, modifiers):

       	if symbol in self.key_pressed:
    	    self.image = self.default
    	    self.key_pressed.remove(symbol)