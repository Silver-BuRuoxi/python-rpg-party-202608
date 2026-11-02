from hero import Hero

class Warrior(Hero):
    def __init__(self, name: str, hp: int = 120, mana: int = 50):
        super().__init__(name, hp)
        self.mana = mana

    def use_special_ability(self) -> str:
        return f"{self.name} unleashes a Power Slash using {self.mana} mana!"