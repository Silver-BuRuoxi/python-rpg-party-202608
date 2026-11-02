class Hero:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def use_special_ability(self) -> str:
        return f"{self.name} uses a basic attack!"
