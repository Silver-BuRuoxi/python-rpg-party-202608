from hero import Hero

class Mage(Hero):
    def __init__(self, name: str, hp: int = 80, mana: int = 100):
        super().__init__(name, hp)
        self.mana = mana

    def use_special_ability(self) -> str:
        return f"{self.name} casts Fireball using {self.mana} mana!"