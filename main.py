from pyglet.window import Window
from pyglet.sprite import Sprite
from loader.animations import nick, background, stage2
from entities import characters
import pyglet


window = Window(800, 600)
batch = pyglet.graphics.Batch()
bg2 = Sprite(img=background, batch=batch)
bg = Sprite(img=background, batch=batch)
hero = characters.Hero(x=window.width/2 , y=window.height/2, batch=batch)
window.push_handlers(hero)
bg_offset = 2
bg2.x = bg.x + bg.width

def update(dt):
   hero.update(dt)

   if hero.keys['right']:
      bg.x -= bg_offset
      bg2.x -= bg_offset
	
   if (bg.x + bg.width) < 800:
      bg2.x = (bg.x + bg.width)
   if (bg2.x + bg2.width) < 800:
      bg.x = bg2.x + bg2.width


@window.event
def on_draw():
	window.clear()
	batch.draw()

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
