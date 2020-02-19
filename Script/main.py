#  Don't steal please lol
#  Finishing Touch / Smash Updating tool

import tkinter as tk
from tkinter.ttk import Combobox
from playerClass import Player
import shutil
p = Player()
P1 = ""
P2 = ""
P1Score = ""
P2Score = ""
P1Char = ""
P2Char = ""
P1Alt = ""
P2Alt = ""
RoundName = ""
PhaseLength_Val = ""


def need_reset():
    """Calls for the values in the input to be reset by using the Player class in playerClass.py"""
    p.reset()
    global P1
    P1 = p.update_tag()
    global P2
    P2 = p.update_tag()
    global P1Score
    P1Score = p.update_score()
    global P2Score
    P2Score = p.update_score()
    global P1Char
    P1Char = p.update_chara()
    global P2Char
    P2Char = p.update_chara()
    global P1Alt
    P1Alt = p.update_alt()
    global P2Alt
    P2Alt = p.update_alt()
    global RoundName
    RoundName = ""
    update()


def update():
    """Updates the files based on the input."""
    P1Portrait = f"../210Script/Character Portraits/{P1Char}/{P1Alt}.png"
    P2Portrait = f"../210Script/Character Portraits/{P2Char}/{P2Alt}.png"
    P1File = open("../210Script/P1.txt", 'w')
    P1File.write(P1)
    P1File.close()
    P2File = open("../210Script/P2.txt", 'w')
    P2File.write(P2)
    P2File.close()
    RoundName_File = open("../210Script/Round.txt", 'w')
    RoundName_File.write(RoundName)
    RoundName_File.close()
    P1ScoreFile = open("../210Script/P1Score.txt", 'w')
    P1ScoreFile.write(P1Score)
    P1ScoreFile.close()
    P2ScoreFile = open("../210Script/P2Score.txt", 'w')
    P2ScoreFile.write(P2Score)
    P2ScoreFile.close()
    P1CharFile = open("../210Script/P1Char.txt", 'w')  # Unnecessary for Finishing Touch
    P1CharFile.write(P1Char)
    P1CharFile.close()
    P2CharFile = open("../210Script/P2Char.txt", 'w')  # Unnecessary for Finishing Touch
    P2CharFile.write(P2Char)
    P2CharFile.close()
    shutil.copy(P1Portrait, 'P1.png')
    shutil.copy(P2Portrait, 'P2.png')
    P1HPFile = f"../210Script/IMG/{PhaseLength_Val}{P2Score}.png"  # Unnecessary for Finishing Touch.
    shutil.copy(P1HPFile, 'P1HP.png')
    P2HPFile = f"../210Script/IMG/{PhaseLength_Val}{P1Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P2HPFile, 'P2HP.png')
    P1ScoreIMG = f"../210Script/IMG/{P1Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P1ScoreIMG, 'P1Score.png')
    P2ScoreIMG = f"../210Script/IMG/{P2Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P2ScoreIMG, 'P2Score.png')


def playerSwitch():
    """In case it's needed, the Switch button works to switch sides. P1>P2 and P2>P1."""
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


def button_Pressed():
    """Gathers box info, then runs the update function."""
    global P1
    P1 = p.update_tag(p_tag=entry1.get())
    global P2
    P2 = p.update_tag(p_tag=entry2.get())
    global P1Score
    P1Score = p.update_score(p_score=entry3.get())
    global P2Score
    P2Score = p.update_score(p_score=entry4.get())
    global P1Char
    P1Char = p.update_chara(p_chara=combo1.get())
    global P2Char
    P2Char = p.update_chara(p_chara=combo2.get())
    global P1Alt
    P1Alt = p.update_alt(p_alt=combo3.get())
    global P2Alt
    P2Alt = p.update_alt(p_alt=combo4.get())
    global RoundName
    RoundName = ""
    roundNo = "" + combo6.get()
    if roundNo == "":
        RoundName = combo5.get()
    elif roundNo != "":
        RoundName = combo5.get() + roundNo
    global PhaseLength_Val
    PhaseLength_Val = combo7.get()
    if P1Alt == "":
        P1Alt = "1"
    if P2Alt == "":
        P2Alt = "1"
    if PhaseLength_Val == "2/3":
        PhaseLength_Val = "23"
    elif PhaseLength_Val == "3/5":
        PhaseLength_Val = "35"
    if PhaseLength_Val == "":
        PhaseLength_Val = "23"

    if P1Alt == "":
        P1Alt = "1"
    if P2Alt == "":
        P2Alt = "1"
    update()


need_reset()  # Calls for the reset function so that it's reset every time the software opens.

#  Replaces the names and pictures, grabbing them from the Character Portraits folder
# (which is located in the Script folder)

# GUI Code Below


win = tk.Tk()
win.title("SASU Stream Updater by Aru")


# Labels

label1 = tk.Label(text="Player 1 Name:").grid(column=0, row=0)
label2 = tk.Label(text="Player 2 Name:").grid(column=0, row=1)
label3 = tk.Label(text="Round Name:").grid(column=0, row=3)
label4 = tk.Label(text="Player 1 Character:").grid(column=0, row=4)
label5 = tk.Label(text="Player 2 Character:").grid(column=0, row=5)
label6 = tk.Label(text="Player 1 Score:").grid(column=0, row=6)
label7 = tk.Label(text="Player 2 Score:").grid(column=2, row=6)
label8 = tk.Label(text="2/3 or 3/5?").grid(column=0, row=2)

# Entry Fields


DropDown1 = ["---SMASH 64---", "Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox",
             "Pikachu", "Luigi", "Ness", "Captain Falcon", "Jigglypuff", "---MELEE---", "Peach", "Daisy", "Bowser",
             "Ice Climbers", "Sheik", "Zelda", "Dr. Mario", "Pichu", "Falco", "Marth", "Lucina", "Young Link",
             "Ganondorf", "Mewtwo", "Roy", "Chrom", "Mr. Game and Watch", "---BRAWL---", "Meta Knight", "Pit",
             "Dark Pit", "Zero Suit Samus", "Wario", "Snake", "Ike", "Pokemon Trainer", "Diddy Kong", "Lucas",
             "Sonic", "King Dedede", "Olimar", "Lucario", "R.O.B", "Toon Link", "Wolf", "---SMASH 4---", "Villager",
             "Wii Fit Trainer", "Rosalina and Luma", "Little Mac", "Greninja", "Mii Swordfighter", "Mii Gunner",
             "Mii Brawler", "Palutena", "PAC-MAN", "Robin", "Shulk", "Bowser Jr", "Duck Hunt", "Ryu", "Ken", "Cloud",
             "Corrin", "Bayonetta", "---ULTIMATE---", "Inkling", "Ridley", "Simon", "Richter", "King K. Rool",
             "Isabelle", "Incineroar",  "Piranha Plant", "Joker", "Hero", "Banjo & Kazooie", "Terry", "Byleth"]

DropDown2 = ["1", "2", "3", "4", "5", "6", "7", "8"]

PhaseNameBox1 = ["Winner's Round", "Loser's Round", "Winner's Quarters", "Winner's Semis", "Winner's Finals",
                 "Loser's Quarters", "Loser's Semis", "Loser's Finals"]

PhaseLength = ["2/3", "3/5"]
entry1 = tk.Entry(win)  # Initializes Player 1 Name Box
entry1.grid(column=2, row=0)
entry2 = tk.Entry(win)  # Initializes Player 2 Name Box
entry2.grid(column=2, row=1)
combo7 = Combobox(win, values=PhaseLength)  # Initializes Phase Length Box
combo7.grid(column=2, row=2)
combo5 = Combobox(win, values=PhaseNameBox1)  # Initializes Phase Name Box
combo5.grid(column=1, row=3)
combo6 = Combobox(win, values=DropDown2)  # Initializes Phase Number Box
combo6.grid(column=2, row=3)
combo1 = Combobox(win, values=DropDown1)  # Initializes Player 1 Character Box
combo1.grid(column=1, row=4)
combo3 = Combobox(win, values=DropDown2)  # Initializes Player 1 Character Alt Box
combo3.grid(column=2, row=4)
combo2 = Combobox(win, values=DropDown1)  # Initializes Player 2 Character Box
combo2.grid(column=1, row=5)
combo4 = Combobox(win, values=DropDown2)  # Initializes Player 2 Character Alt Box
combo4.grid(column=2, row=5)
entry3 = tk.Entry(win)  # Initializes Player 1 Score Box
entry3.grid(column=0, row=7)
entry3.insert(string="0", index="0")
entry4 = tk.Entry(win)  # Initializes Player 2 Score Box
entry4.grid(column=2, row=7)
entry4.insert(string="0", index="0")

#  Update Button
button1 = tk.Button(text="Update", command=button_Pressed, height="3", width="20")
button1.grid(column=1, row=7)

#  Switch Button
button2 = tk.Button(text="Switch Players", command=playerSwitch, height="1", width="20")
button2.grid(column=1, row=8)

#  Dropdown Menu

menu = tk.Menu(win)
win.config(menu=menu)

subMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Commands", menu=subMenu)
subMenu.add_command(label="Reset", command=need_reset)
subMenu.add_command(label="Update", command=button_Pressed)


stMenu = tk.Menu(menu, tearoff=0)
subMenu2 = tk.Menu(menu)
menu.add_cascade(label="Misc.", menu=stMenu)

win.mainloop()
