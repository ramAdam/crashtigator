import cocos
from cocos.director import director
from loader.animations import nick
from cocos.sprite import Sprite
import pyglet


class Character(cocos.layer.Layer):
    
    is_event_handler = True

    def __init__(self):
        super(Character, self).__init__()
        self.controls = dict(up=False, down=False, right=False, left=False, shoot=False)
        x, y = director.get_window_size()
        
        self.idle = Sprite(nick.get('idle'))
        self.walk = Sprite(nick.get("walk"))
        self.shoot = Sprite(nick.get("shoot"))
                
        self.default = Sprite(self.idle.image)
        self.default.position = x/2, y/2
        
        self.add(self.default)

    def update_anim(self, anim):
        self.default.image = anim.image

    
    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.RIGHT:
            self.controls['right'] = True
            self.update_anim(self.walk)
        if key == pyglet.window.key.S:
            self.controls['shoot'] = True
            self.update_anim(self.shoot)
            
        


    def on_key_release(self, key, modifiers):
        if self.controls['right']:
            self.controls['right'] = False
        if self.controls['shoot']:
            self.controls['shoot'] = False

        self.update_anim(self.idle)
		
		




		



