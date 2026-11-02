from hero import Hero

class Healer(Hero):
    def __init__(self, name, hp = 60, mana = 80):
        super().__init__(name, hp)
        self.mana = mana

    def heal(self, hero):
        self.mana -= 5
        return(f"Heals {hero}!")