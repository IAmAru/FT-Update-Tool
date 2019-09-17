#don't steal please lol
#Finishing Touch / Smash Updating tool

import tkinter as tk
from tkinter import StringVar
from tkinter.ttk import Combobox
import os
import shutil
import sys

#Reset; sets every value to the starting position. Stream shows no names in the boxes and makes all the pictures white

def reset():
    player1_file=open("../Script/Player1.txt",'w')
    player2_file=open("../Script/Player2.txt",'w')
    roundname_file=open("../Script/Round.txt",'w')
    player1s_file=open("../Script/Player 1 Score.txt","w")
    player2s_file=open("../Script/Player 2 Score.txt","w")
    player1s_file.write('0')
    player1s_file.close()
    player2s_file.write('0')
    player2s_file.close()
    p1_portrait="../Script/Character Portraits/Blank.png"
    try:
        shutil.copy(p1_portrait,'P1.png')
    except Exception as e:
        print(e)
    p2_portrait="../Script/Character Portraits/Blank.png"
    try:
       shutil.copy(p2_portrait,'P2.png')
    except Exception as e:
        print(e)

reset()

#Stream Update Function... What happens when the 'Update' Button is pressed.
        
def streamupdate():

# Gathers info from the boxes.
    
    player1 = entry1.get()
    player2 = entry2.get()
    roundnumber = " " + combo6.get()

    if roundnumber == " ":
        roundname = combo5.get()
    elif roundnumber != " ":
        roundname = combo5.get() + roundnumber

    player1score = entry4.get()
    player2score = entry5.get()
    player1char = combo1.get()
    player2char = combo2.get()
    player1alt = combo3.get()
    player2alt = combo4.get()

# This is a failsafe in case the alt box is not filled out. In case the output from .get() does not equal to 1-8, it'll default to 1 as to not throw an exception.

    if player1alt not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        player1alt = "1"

    if player2alt not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        player2alt = "1"

#Replaces the names and pictures, grabbing them from the Character Portaits folder (which is located in the Script folder)
        
    srcfile_p1="../Script/Character Portraits/" + player1char + '/' + player1alt + '.png'
    srcfile_p2="../Script/Character Portraits/" + player2char + '/' + player2alt + '.png'
    player1_file=open("../Script/Player1.txt",'w')
    player2_file=open("../Script/Player2.txt",'w')
    roundname_file=open("../Script/Round.txt",'w')
    player1s_file=open("../Script/Player 1 Score.txt",'w')
    player2s_file=open("../Script/Player 2 Score.txt",'w')
    player1_file.write(player1)
    player2_file.write(player2)
    roundname_file.write(roundname)
    player1s_file.write(player1score)
    player2s_file.write(player2score)
    player1_file.close()
    player2_file.close()
    roundname_file.close()
    player1s_file.close()
    player2s_file.close()
    try:
        shutil.copy(srcfile_p1,'P1.png')
    except Exception as e:
        print(e)

    try:
        shutil.copy(srcfile_p2,'P2.png')
    except Exception as e:
        print(e)

#Credits meme
    
creditsmsg = "Credits:\n\n *HHIG | Aru\n-Basically all the work.\n\n*Monika\n-Keeping Aru alive.\n\n*HHIG | Red\n-Debugging, overhaul of 'go back' in version 0.2.0.\n\n*Conker (Oscar)\n-Being the most frequent user/reporting some bugs\n\nFollow me on Twitter: @Aru_star_\n\nSpecial Thanks:\n Special thanks to Andrew Rodriguez (HHIG | Red) for helping me test \n/ debug this mess. Additionally, super thanks to PLAYlive Nation \n for hosting my tournaments, Oscar for being my best and most frequent\n user, christmasbob1 for replacing me, and HHIG for existing. \nThanks to everyone!\n\n -HHIG | Aru"

def crdts():
    popup2 = tk.Tk()
    popup2.geometry("500x500")
    popup2.title("Credits")
    label = tk.Label(popup2, text=creditsmsg)
    label.pack(side="top", fill="x", pady=10)
    popup2.mainloop()

#GUI Code Below

win = tk.Tk()
win.title("Finishing Touch Stream Updater")


#Labels

label1 = tk.Label(text="Player 1 Name:").grid(column=0, row=1)
label2 = tk.Label(text="Player 2 Name:").grid(column=0, row=2)
label3 = tk.Label(text="Round Name:").grid(column=0, row=3)
label4 = tk.Label(text="Player 1 Character/Alt:").grid(column=0, row=4)
label5 = tk.Label(text="Player 2 Character/Alt:").grid(column=0, row=5)
label6 = tk.Label(text="Player 1 Score:").grid(column=0, row=6)
label7 = tk.Label(text="Player 2 Score:").grid(column=2, row=6)

#Entry Fields

entry1 = tk.Entry(win)
entry1.grid(column=2, row=1)
entry2 = tk.Entry(win)
entry2.grid(column=2, row=2)
entry4 = tk.Entry(win)
entry4.grid(column=0, row=7)
entry4.insert(string="0", index="0")
entry5 = tk.Entry(win)
entry5.grid(column=2,row=7)
entry5.insert(string="0", index="0")

ddl1 = "---SMASH 64---", "Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox", "Pikachu", "Luigi", "Ness", "Captain Falcon", "Jigglypuff", "---MELEE---", "Peach", "Daisy", "Bowser", "Ice Climbers", "Sheik", "Zelda", "Dr. Mario", "Pichu", "Falco", "Marth", "Lucina", "Young Link", "Ganondorf", "Mewtwo", "Roy", "Chrom", "Mr. Game and Watch", "---BRAWL---", "Meta Knight", "Pit", "Dark Pit", "Zero Suit Samus", "Wario", "Snake", "Ike", "Pokemon Trainer", "Diddy Kong", "Lucas", "Sonic", "King Dedede", "Olimar", "Lucario", "R.O.B", "Toon Link", "Wolf", "---SMASH 4---", "Villager", "Wii Fit Trainer", "Rosalina and Luma", "Little Mac", "Greninja", "Mii Swordfighter", "Mii Gunner", "Mii Brawler", "Palutena", "PAC-MAN", "Robin", "Shulk", "Bowser Jr", "Duck Hunt", "Ryu", "Ken", "Cloud", "Corrin", "Bayonetta", "---ULTIMATE---", "Inkling", "Ridley", "Simon", "Richter", "King K. Rool", "Isabelle", "Incineroar",  "Piranha Plant", "Joker", "Hero", "Banjo & Kazooie", "Viewtiful Joe"
ddl2 = "1", "2", "3", "4", "5", "6", "7", "8"
phasename1 = "Winner's Round", "Loser's Round", "Winner's Quarters", "Winner's Semis", "Winner's Finals", "Loser's Quarters", "Loser's Semis", "Loser's Finals"
combo1 = Combobox(win, values=ddl1)
combo1.grid(column=1, row=4)
combo2 = Combobox(win, values=ddl1)
combo2.grid(column=1, row=5)
combo3 = Combobox(win, values=ddl2)
combo3.grid(column=2, row=4)
combo4 = Combobox(win, values=ddl2)
combo4.grid(column=2, row=5)
combo5 = Combobox(win, values=phasename1)
combo5.grid(column=1, row=3)
combo6 = Combobox(win, values=ddl2)
combo6.grid(column=2, row=3)

#Button
button1 = tk.Button(text="Update", command=streamupdate, height="3", width="20")
button1.grid(column=1, row=7)

#Menu

menu = tk.Menu(win)
win.config(menu=menu)

subMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Commands", menu=subMenu)
subMenu.add_command(label="Reset", command=reset)
subMenu.add_command(label="Update", command=streamupdate)


stMenu = tk.Menu(menu, tearoff=0)
subMenu2 = tk.Menu(menu)
menu.add_cascade(label="Misc.", menu=stMenu)
stMenu.add_command(label="Credits", command=crdts)

win.mainloop()
