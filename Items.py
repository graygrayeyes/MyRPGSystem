

class Item:
    def __init__(self, name, weight=1, worth=0, small=True):
        self.name = name
        self.weight = weight
        self.worh = worth
        self.small = small

class Container(Item): # позволяет носить size вещей типа small
    def __init__(self, name, weight=1, worth=0, size=1):
        Item.__init__(self, name, weight, worth, False)
        self.max_size = size

# ***** WEAPONS ********
# ***** Abstract weapon classes ******
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

# ***** Certain weapon classes. Melee_Weapon ******
# Improvised
class Improvised(Melee_Weapon):
    def __init__(self, name="improvised", weight=1, worth=0, small=False, required_strength=1,
                 base_damage=0, armor_piercing=0, properties=set('crushing', 'unsuited_for_parry(19..20)'),
                 two_handed=False):
        Melee_Weapon.__init__(self, name, weight, worth, small, required_strength,
                              base_damage, armor_piercing, properties, two_handed)

# one-handed
class Knuckle(Melee_Weapon):
    def __init__(self, name="knuckle", weight=1, worth=10, small=True,
                 base_damage=0, armor_piercing=0, properties=set('crushing')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class Dagger(Melee_Weapon):
    def __init__(self, name="dagger", weight=2, worth=10, small=False,
                 base_damage=1, armor_piercing=0, properties=set('for_parry')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class One_Handed_Sword(Melee_Weapon):
    def __init__(self, name="one_handed_sword", weight=4, worth=110, small=False,
                 base_damage=2, armor_piercing=0, properties=set('for_parry', '+2 Attak, +2 Parry')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class Axe (Melee_Weapon):
    def __init__(self, name="axe", weight=4, worth=40, small=False,
                 base_damage=2, armor_piercing=1, properties=set('unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class Mace (Melee_Weapon):
    def __init__(self, name="mace", weight=5, worth=50, small=False,
                 base_damage=2, armor_piercing=0, properties=set('crushing', 'unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

# two-handed
class Two_Handed_Sword(Melee_Weapon):
    def __init__(self, name="two_handed_sword", weight=8, worth=160, small=False,
                 base_damage=3, armor_piercing=0, properties=set('for_parry', '+2 Attak, +2 Parry')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=True, required_strength=1)

class Battle_Axe (Melee_Weapon):
    def __init__(self, name="battle_axe", weight=8, worth=100, small=False,
                 base_damage=3, armor_piercing=1, properties=set('unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=True, required_strength=1)

class Warhammer (Melee_Weapon):
    def __init__(self, name="warhammer", weight=9, worth=100, small=False,
                 base_damage=3, armor_piercing=0, properties=set('crushing', 'unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=True, required_strength=1)

class Spear (Melee_Weapon):
    def __init__(self, name="spear", weight=5, worth=50, small=False,
                 base_damage=3, armor_piercing=0, properties=set('preemptive attack', 'unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=True, required_strength=1)

class Halberd (Melee_Weapon):
    def __init__(self, name="halberd", weight=6, worth=70, small=False,
                 base_damage=3, armor_piercing=1,
                 properties=set('preemptive attack(AP=0)', 'unsuited_for_parry(19..20)')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=True, required_strength=1)

# shields
class Buckler (Melee_Weapon):
    def __init__(self, name="buckler", weight=3, worth=40, small=False,
                 base_damage=0, armor_piercing=0,
                 properties=set('crushing', 'shield')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class Medium_Shield (Melee_Weapon):
    def __init__(self, name="medium_shield", weight=5, worth=50, small=False,
                 base_damage=1, armor_piercing=0,
                 properties=set('crushing', 'shield', '+3 shield',
                                '-1 strong_hit', '-3 accuracy_hit', '-1 firearm incoming attack')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)

class Large_Shield (Melee_Weapon):
    def __init__(self, name="large_shield", weight=7, worth=70, small=False,
                 base_damage=1, armor_piercing=0,
                 properties=set('crushing', 'shield', '+5 shield',
                                '-2 strong_hit', '-5 accuracy_hit', '-2 firearm incoming attack')):
        Melee_Weapon.__init__(self, name, weight, worth, small, base_damage, armor_piercing,
                              properties, two_handed=False, required_strength=1)
# ***** Certain weapon classes. Throwing_Weapon ******

# ***** Certain weapon classes. Range_Weapon ******


# *****END WEAPONS ********