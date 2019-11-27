from Weapons_Abstract import *

# Improvised
class Improvised(Melee_Weapon):
    def __init__(self, name="improvised", weight=1, worth=0, small=False, required_strength=1,
                 base_damage=0, armor_piercing=0,  two_handed=False):
        Melee_Weapon.__init__(self, name, weight, worth, small, required_strength,
                              base_damage, armor_piercing, two_handed,
                              properties=set('crushing', 'unsuited_for_parry(19..20)') )

# one-handed
class Knuckle(Melee_Weapon):
    def __init__(self, name="knuckle"):
        Melee_Weapon.__init__(self, name, weight=1, worth=10, small=True, base_damage=0, armor_piercing=0,
                              properties=set('crushing'), two_handed=False, required_strength=1)

class Dagger(Melee_Weapon):
    def __init__(self, name="dagger"):
        Melee_Weapon.__init__(self, name, weight=2, worth=10, small=False, base_damage=1, armor_piercing=0,
                              properties=set('for_parry'), two_handed=False, required_strength=1)

class One_Handed_Sword(Melee_Weapon):
    def __init__(self, name="one_handed_sword"):
        Melee_Weapon.__init__(self, name, weight=4, worth=11, small=False, base_damage=2, armor_piercing=0,
                              properties=set('for_parry', '+2 Attak, +2 Parry'), two_handed=False, required_strength=1)

class Axe (Melee_Weapon):
    def __init__(self, name="axe"):
        Melee_Weapon.__init__(self, name, weight=4, worth=40, small=False, base_damage=2, armor_piercing=1,
                              propertiesproperties=set('unsuited_for_parry(19..20)'),
                              two_handed=False, required_strength=1)

class Mace (Melee_Weapon):
    def __init__(self, name="mace"):
        Melee_Weapon.__init__(self, name, weight=5, worth=50, small=False, base_damage=2, armor_piercing=0,
                              properties=set('crushing', 'unsuited_for_parry(19..20)'),
                              two_handed=False, required_strength=1)

# two-handed
class Two_Handed_Sword(Melee_Weapon):
    def __init__(self, name="two_handed_sword"):
        Melee_Weapon.__init__(self, name, weight=8, worth=160, small=False, base_damage=3, armor_piercing=0,
                              properties=set('for_parry', '+2 Attak, +2 Parry'), two_handed=True, required_strength=1)

class Battle_Axe (Melee_Weapon):
    def __init__(self, name="battle_axe"):
        Melee_Weapon.__init__(self, name, weight=8, worth=100, small=False, base_damage=3, armor_piercing=1,
                              properties=set('unsuited_for_parry(19..20)'), two_handed=True, required_strength=1)

class Warhammer (Melee_Weapon):
    def __init__(self, name="warhammer"):
        Melee_Weapon.__init__(self, name, weight=9, worth=100, small=False, base_damage=3, armor_piercing=0,
                              properties=set('crushing', 'unsuited_for_parry(19..20)'),
                              two_handed=True, required_strength=1)

class Spear (Melee_Weapon):
    def __init__(self, name="spear"):
        Melee_Weapon.__init__(self, name, weight=5, worth=50, small=False, base_damage=3, armor_piercing=0,
                              properties=set('distance_attack', 'unsuited_for_parry(19..20)'),
                              two_handed=True, required_strength=1)

class Halberd (Melee_Weapon):
    def __init__(self, name="halberd"):
        Melee_Weapon.__init__(self, name, weight=6, worth=70, small=False, base_damage=3, armor_piercing=1,
                              properties=set('distance_attack(AP=0)', 'unsuited_for_parry(19..20)'),
                              two_handed=True, required_strength=1)

# shields
class Buckler (Melee_Weapon):
    def __init__(self, name="buckler"):
        Melee_Weapon.__init__(self, name, weight=3, worth=40, small=False, base_damage=0, armor_piercing=0,
                              properties=set('crushing', 'shield'), two_handed=False, required_strength=1)

class Medium_Shield (Melee_Weapon):
    def __init__(self, name="medium_shield"):
        Melee_Weapon.__init__(self, name, weight=5, worth=50, small=False, base_damage=1, armor_piercing=0,
                              properties=set('crushing', 'shield', '+3 shield',
                                '-1 strong_hit', '-3 accuracy_hit', '-1 firearm incoming attack'),
                              two_handed=False, required_strength=1)

class Large_Shield (Melee_Weapon):
    def __init__(self, name="large_shield"):
        Melee_Weapon.__init__(self, name, weight=7, worth=70, small=False, base_damage=1, armor_piercing=0,
                              properties=set('crushing', 'shield', '+5 shield',
                                '-2 strong_hit', '-5 accuracy_hit', '-2 firearm incoming attack'),
                              two_handed=False, required_strength=1)