from pyglet.window import Window

import pyglet
from loader.animations import nick
from entities import characters
import copy


window = Window(800, 600)
batch = pyglet.graphics.Batch()
hero = characters.Hero(nick.get("idle"), batch=batch)
window.push_handlers(hero)

		
@window.event
def on_draw():
	window.clear()
	batch.draw()
	
if __name__ == "__main__":
	pyglet.app.run()
