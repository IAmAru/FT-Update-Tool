from playerClass import Player
from updateFunction import update
p = Player()


def button_Pressed():
    """Gathers box info, then runs the update function."""
    from gui import entry1, entry2, entry3, entry4, combo1, combo2, combo3, combo4, combo5, combo6, combo7
    P1Button = p.update_tag(p_tag=entry1.get())
    P2Button = p.update_tag(p_tag=entry2.get())
    P1ScoreButton = p.update_score(p_score=entry3.get())
    P2ScoreButton = p.update_score(p_score=entry4.get())
    P1CharButton = p.update_chara(p_chara=combo1.get())
    P2CharButton = p.update_chara(p_chara=combo2.get())
    P1AltButton = p.update_alt(p_alt=combo3.get())
    P2AltButton = p.update_alt(p_alt=combo4.get())
    RoundNameButton = ""
    roundNoButton = "" + combo6.get()
    if roundNoButton == "":
        RoundNameButton = combo5.get()
    elif roundNoButton != "":
        RoundNameButton = f"{combo5.get()} {roundNoButton}"
    PhaseLength_Val_Button = combo7.get()
    if P1AltButton == "":
        P1AltButton = "1"
    if P2AltButton == "":
        P2AltButton = "1"
    if PhaseLength_Val_Button == "2/3":
        PhaseLength_Val_Button = "23"
    elif PhaseLength_Val_Button == "3/5":
        PhaseLength_Val_Button = "35"
    if PhaseLength_Val_Button == "":
        PhaseLength_Val_Button = "23"
    update(P1=P1Button, P2=P2Button, P1Score=P1ScoreButton, P2Score=P2ScoreButton, P1Char=P1CharButton,
           P2Char=P2CharButton, P1Alt=P1AltButton, P2Alt=P2AltButton, RoundName=RoundNameButton,
           PhaseLength_Val=PhaseLength_Val_Button)