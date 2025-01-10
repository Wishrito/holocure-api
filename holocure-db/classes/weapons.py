from enum import Enum


class Upgrade:
    def __init__(self, level: int, description: str):
        self.level = level
        self.description = description


class WeaponType(Enum):
    MELEE = "Melee"
    RANGED = "Ranged"
    MULTISHOT = "Multishot"


class Weapon:
    def __init__(self, weaponData: dict):
        self.name = weaponData.get("name")
        self.description = weaponData.get("description")
        self.weaponType = weaponData.get("weaponType")
        self.upgrades: list[Upgrade] = [
            Upgrade(upgrade) for upgrade in weaponData.get("upgrades")]

    def __str__(self):
        return f"{self.name} : {self.description}"


class Collab(Weapon):
    def __init__(self, name: str, description: str, weapon1: Weapon, weapon2: Weapon, weaponType: WeaponType):
        super().__init__(name, description, weaponType)
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        delattr(self, "upgrades")

    def __str__(self):
        return f"{self.name} (weapon1 : {self.weapon1} + weapon2 : {self.weapon2}) : {self.description}"


flatteningBoard = Collab()

print(flatteningBoard)
