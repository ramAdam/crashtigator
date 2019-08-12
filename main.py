from pyglet.window import Window
import pyglet
from loader.animations import nick
from entities import characters



window = Window(800, 600)
batch = pyglet.graphics.Batch()
hero = characters.Hero(batch=batch)
window.push_handlers(hero)

def update(dt):
	hero.update(dt)

@window.event
def on_draw():
	window.clear()
	batch.draw()
	
if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
