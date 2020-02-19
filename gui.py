import tkinter as tk
from tkinter.ttk import Combobox
from resetFunction import reset_func
from updateButtonPressed import button_Pressed
from switchFunction import playerSwitch

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
subMenu.add_command(label="Reset", command=reset_func)
subMenu.add_command(label="Update", command=button_Pressed)


stMenu = tk.Menu(menu, tearoff=0)
subMenu2 = tk.Menu(menu)
menu.add_cascade(label="Misc.", menu=stMenu)

win.mainloop()
