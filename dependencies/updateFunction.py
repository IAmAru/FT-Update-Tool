import shutil


def update(P1, P2, P1Score, P2Score, P1Char, P2Char, P1Alt, P2Alt, Round, PhaseLength_Val):
    filename = [P1, P2, P1Score, P2Score, P1Char, P2Char, Round]
    filename_str = ["P1", "P2", "P1Score", "P2Score", "P1Char", "P2Char", "Round"]
    for x in filename:
        index = filename.index(x)
        with open(f'Output/{filename_str[index]}.txt', 'w') as file_object:
            file_object.write(x)
    shutil.copy(f"Character Portraits/{P1Char}/{P1Alt}.png", 'Output/P1.png')
    shutil.copy(f"Character Portraits/{P2Char}/{P2Alt}.png", 'Output/P2.png')
    shutil.copy(f"IMG/{PhaseLength_Val}{P2Score}.png", 'Output/P1HP.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{PhaseLength_Val}{P1Score}.png", 'Output/P2HP.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{P1Score}.png", 'Output/P1Score.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{P2Score}.png", 'Output/P2Score.png')  # Unnecessary for Finishing Touch
