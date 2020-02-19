class Player:

    """An attempt to represent a Smash Player."""

    def __init__(self, tag="", chara="Blank", alt="1", score="0"):
        self.tag = tag
        self.chara = chara
        self.alt = alt
        self.score = score

    def update_tag(self, p_tag=""):
        self.tag = p_tag
        return self.tag

    def update_chara(self, p_chara="Blank"):
        self.chara = p_chara
        return self.chara

    def update_alt(self, p_alt="1"):
        self.alt = p_alt
        return self.alt

    def update_score(self, p_score="0"):
        self.score = p_score
        return self.score

    def reset(self):
        self.tag = ""
        self.score = "0"
        self.alt = "1"
        self.chara = "Blank"
