from dependencies.playerClass import Player
from dependencies.updateButtonPressed import button_Pressed

p = Player()


def playerSwitch():
    from dependencies.gui import entry1, entry2, entry3, entry4, combo1, combo2, combo3, combo4
    """In case it's needed, the Switch button works to switch sides. P1>P2 and P2>P1. I think it'd be really good if
    I could find a better way to go about it, without many lines or it being so awkward. I'll see what I can do."""
    P1Box = entry1.get()
    P2Box = entry2.get()
    P1ScoreBox = entry3.get()
    P2ScoreBox = entry4.get()
    P1CharaBox = combo1.get()
    P2CharaBox = combo2.get()
    P1AltBox = combo3.get()
    P2AltBox = combo4.get()
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    combo1.delete(0, 'end')
    combo2.delete(0, 'end')
    combo3.delete(0, 'end')
    combo4.delete(0, 'end')
    entry1.insert(string=P2Box, index="0")
    entry2.insert(string=P1Box, index="0")
    entry3.insert(string=P2ScoreBox, index="0")
    entry4.insert(string=P1ScoreBox, index="0")
    combo1.insert(string=P2CharaBox, index="0")
    combo2.insert(string=P1CharaBox, index="0")
    combo3.insert(string=P2AltBox, index="0")
    combo4.insert(string=P1AltBox, index="0")
    button_Pressed()
