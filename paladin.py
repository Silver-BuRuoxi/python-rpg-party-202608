from hero import Hero

class Paladin(Hero):
    def __init__(self, name: str, hp: int = 80, intelligence: int = 100):
        super().__init__(name, hp)
        self.intelligence = intelligence

    def use_special_ability(self) -> str:
        self.hp*=2
        self.intelligence*=2
        return f"{self.name} have sanctioned you in the name of justice!"

#test