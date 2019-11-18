from cocos.scene import Scene
from cocos.director import director
from entities.characters import Character


if __name__ == "__main__":
   
    director.init()
    director.run(Scene(Character()))