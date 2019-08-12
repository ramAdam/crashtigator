from pyglet import resource

resource.path = ['./asset']
resource.reindex()


nick = dict(walk=resource.animation('nick_walk.gif'),
            shoot=resource.animation('nick_shoot.gif'),
            idle=resource.animation('nick_fury_stand.gif') 
)


kitten = resource.image("kitten.png")
