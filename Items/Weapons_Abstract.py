from Items_Abstract import *

class Weapon (Item):
    def __init__(self, name, weight=1, worth=0, small=True, required_strength=1,
                 base_damage=0, armor_piercing=0, properties=set(), two_handed=False):
        Item.__init__(self, name, weight, worth, small)
        self.base_damage = base_damage
        self.armor_piercing = armor_piercing
        self.properties = properties
        self.two_handed = two_handed
        self.required_strength = required_strength

class Melee_Weapon(Weapon):
    def __init__(self, name, weight=1, worth=0, small=True, required_strength=1,
                 base_damage=0, armor_piercing=0, properties=set(), two_handed=False):
        Weapon.__init__(self, name, weight, worth, small, required_strength,
                        base_damage, armor_piercing, properties, two_handed)

class Throwing_Weapon(Weapon):
    def __init__(self, name, weight=1, worth=0, small=True, required_strength=1,
                 base_damage=0, armor_piercing=0, properties=set(),  distance=1):
        Weapon.__init__(self, name, weight, worth, small, required_strength,
                        base_damage, armor_piercing, properties, two_handed=False)
        self.distance = distance

class Range_Weapon(Weapon):
    def __init__(self, name, weight=1, worth=0, small=True, required_strength=1,
                 base_damage=0, armor_piercing=0, properties=set(), two_handed=True, distance=1, reload_time=0):
        Weapon.__init__(self, name, weight, worth, small, required_strength,
                        base_damage, armor_piercing, properties, two_handed)
        self.distance = distance
        self.reload_time = reload_time
