from deck import Deck
from ui import Button

class Facade:

    def __init__(self):
        self.deck=Deck()
        self.buttons=[]

    def loadGame(self,dimensions,color):
        undo_button = Button(dimensions, "Отмена", (10, 10), (50, 30), color, centered=False, text_size=11, action="undo")
        pause_button = Button(dimensions, "Пауза", (dimensions[0]-50, 10), (40, 30), color, centered=False, text_size=10, action="pause")
        self.buttons.append(undo_button)
        self.buttons.append(pause_button)
        self.deck.load_cards()
        self.deck.shuffle_cards()
        self.deck.load_piles(dimensions)
        