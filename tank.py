from hero import Hero


class Tank(Hero):
    def __init__(self, name: str, hp: int, shield: int):
        super().__init__(name, hp)
        self.shield = shield

    def use_special_ability(self) -> str:
        self.shield = 20
        return "Shield activated"

    def shield_damage(self, damage: int):
        self.shield = max(0, self.shield - damage)

    def take_damage(self, damage: int):
        if damage <= self.shield:
            self.shield_damage(damage)
        else:
            remaining_damage = damage - self.shield
            self.shield_damage(self.shield)
            self.shield = 0
            self.hp = max(0, self.hp - remaining_damage)
