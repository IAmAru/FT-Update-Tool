import shutil


def update(P1, P2, P1Score, P2Score, P1Char, P2Char, P1Alt, P2Alt, RoundName, PhaseLength_Val):
    """Updates the files based on the input."""
    P1Portrait = f"../210Script/Character Portraits/{P1Char}/{P1Alt}.png"
    P2Portrait = f"../210Script/Character Portraits/{P2Char}/{P2Alt}.png"
    P1File = open("../210Script/Output/P1.txt", 'w')
    P1File.write(P1)
    P1File.close()
    P2File = open("../210Script/Output/P2.txt", 'w')
    P2File.write(P2)
    P2File.close()
    RoundName_File = open("../210Script/Output/Round.txt", 'w')
    RoundName_File.write(RoundName)
    RoundName_File.close()
    P1ScoreFile = open("../210Script/Output/P1Score.txt", 'w')
    P1ScoreFile.write(P1Score)
    P1ScoreFile.close()
    P2ScoreFile = open("../210Script/Output/P2Score.txt", 'w')
    P2ScoreFile.write(P2Score)
    P2ScoreFile.close()
    P1CharFile = open("../210Script/Output/P1Char.txt", 'w')  # Unnecessary for Finishing Touch
    P1CharFile.write(P1Char)
    P1CharFile.close()
    P2CharFile = open("../210Script/Output/P2Char.txt", 'w')  # Unnecessary for Finishing Touch
    P2CharFile.write(P2Char)
    P2CharFile.close()
    shutil.copy(P1Portrait, '../210Script/Output/P1.png')
    shutil.copy(P2Portrait, '../210Script/Output/P2.png')
    P1HPFile = f"../210Script/IMG/{PhaseLength_Val}{P2Score}.png"  # Unnecessary for Finishing Touch.
    shutil.copy(P1HPFile, '../210Script/Output/P1HP.png')
    P2HPFile = f"../210Script/IMG/{PhaseLength_Val}{P1Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P2HPFile, '../210Script/Output/P2HP.png')
    P1ScoreIMG = f"../210Script/IMG/{P1Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P1ScoreIMG, '../210Script/Output/P1Score.png')
    P2ScoreIMG = f"../210Script/IMG/{P2Score}.png"  # Unnecessary for Finishing Touch
    shutil.copy(P2ScoreIMG, '../210Script/Output/P2Score.png')
