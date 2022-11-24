from ursina import *

class card(Entity):
    def __init__(self, card_texture):
        super().__init__(
        model = "quad",
        scale = (2.5, 3.5, 1),
        collider = "box",
        color = rgb(255,255,255),
        position = (0, 0, 0),
        texture = card_texture
        )
        
app = Ursina()

card1 = card('assets/cards/temp_card.png')

app.run()
        
        
        
