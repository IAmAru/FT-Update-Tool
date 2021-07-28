import shutil


def update(P1="", P2="", P1Score="0", P2Score="0", P1Char="",
           P2Char="", P1Alt="1", P2Alt="1", Round="", PhaseLength_Val="23"):

    """Takes the args for basically everything it needs, digs them from what the gui boxes defines them as. Really,
    it's only called when the button is pressed and when the software starts."""

    filename = [P1, P2, P1Score, P2Score, P1Char, P2Char, Round]
    filename_str = ["P1", "P2", "P1Score", "P2Score", "P1Char", "P2Char", "Round"]

    index = 0

    for i in filename:
        # I'm sick for this one c'mon
        with open(f'Output/{filename_str[index]}.txt', 'w') as file_object:
            file_object.write(i)
            file_object.close()
        print(f"{filename_str[index]} = {filename[index]}")
        index += 1
    

    # The following are "Unnecessary" for Finishing Touch, but they're used specifically for another event,
    # Flare Blade Fridays in updating a health bar and a score.

    shutil.copy(f"IMG/{PhaseLength_Val}{P2Score}.png", 'Output/P1HP.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{PhaseLength_Val}{P1Score}.png", 'Output/P2HP.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{P1Score}.png", 'Output/P1Score.png')  # Unnecessary for Finishing Touch
    shutil.copy(f"IMG/{P2Score}.png", 'Output/P2Score.png')  # Unnecessary for Finishing Touch
