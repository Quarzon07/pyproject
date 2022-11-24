from ursina import *

class card(Entity):
    def __init__(self):
        super().__init__(
        model = "quad",
        scale = (2.5, 3.5, 1),
        collider = "box",
        color = rgb(255,255,255),
        position = (0, 0, 0)
        )
        
app = Ursina()

card1 = card()

app.run()
        
        
        
