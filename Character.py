from Dice_Roll import *
from Common_Consts import *
from Skills_Talents_Traits import *

class Character:
    def __init__(self, characteristics, skills, talents, equipment):
        # Set characteristics, skills, talents
        self.skills = {}
        self.talents = set()
        self.characteristics = {'S': characteristics['S'], # strength
                                'A': characteristics['A'], # agility
                                'T': characteristics['T'], # toughness
                                'P': characteristics['P'], # perception
                                'I': characteristics['I'], # intellect
                                'WP': characteristics['WP'], # will_power
                                'C': characteristics['C']} # charisma

        for key, value in skills.items():
            self.skills[key] = value

        self.talents = self.talents | talents

        if(debug_flag):
            for key in characteristics:
                print(key, ':', self.characteristics[key] )
            print(self.skills)
            print(self.talents)

        # Set health
        self.compute_max_health()
        self.set_current_health_to_max()
        if (debug_flag):
            for key in self.current_health:
                print(key, ':', self.current_health[key])

        # Set equipment
        self.equipment = {'H': equipment['H'],
                          'B': equipment['B'],
                          'L': equipment['L'],
                          'LA': equipment['LA'],
                          'RA': equipment['RA']}

    def compute_max_health(self):
        T_bonus = self.compute_chr_bonus('T')
        if (T_bonus == 0):
            self.max_health = {'H': 1, 'LA': 1, 'RA': 1, 'B': 2, 'LL': 1, 'RL': 1}
        elif (T_bonus == 1):
            self.max_health = {'H': 1, 'LA': 1, 'RA': 1, 'B': 3, 'LL': 1, 'RL': 1}
        elif (T_bonus == 2):
            self.max_health = {'H': 2, 'LA': 2, 'RA': 2, 'B': 4, 'LL': 2, 'RL': 2}
        elif (T_bonus == 3):
            self.max_health = {'H': 3, 'LA': 3, 'RA': 3, 'B': 5, 'LL': 3, 'RL': 3}
        elif (T_bonus == 4):
            self.max_health = {'H': 4, 'LA': 4, 'RA': 4, 'B': 6, 'LL': 4, 'RL': 4}
        elif (T_bonus >= 5):
            self.max_health = {'H': 4, 'LA': 4, 'RA': 4, 'B': 7, 'LL': 4, 'RL': 4}

    def set_current_health_to_max(self):
        self.current_health = {'H': self.max_health['H'],
                               'LA': self.max_health['LA'],
                               'RA': self.max_health['RA'],
                               'B': self.max_health['B'],
                               'LL': self.max_health['LL'],
                               'RL': self.max_health['RL']}

    def compute_chr_bonus(self, chr_name):
        return int(self.characteristics[chr_name]/10)

# class Health:
#     def __init__(self, toughness_bonus):

class Body_Part:
    def __init__(self, type, toughness_bonus):
        self.type = type # 'H', 'LA', 'RA', 'B', 'LL', 'RL'
        self.max_health = self.compute_max_health(toughness_bonus)
        self.current_health = self.max_health
        self.critical_injurys = [False, False, False, False]

    def update_part(self, toughness_bonus):
        self.max_health = self.compute_max_health(toughness_bonus)
        self.current_health = self.max_health

    def compute_max_health(self, toughness_bonus):
        health_range_body = [2, 3, 4, 5, 6, 7]
        health_range_other_parts = [1, 1, 2, 3, 4, 5]
        if(self.type == 'B'):
            return health_range_body[toughness_bonus]
        else: # H, RA, LA, LL, RL
            return health_range_other_parts[toughness_bonus]

    def get_hit_or_heal(self, damage):
        self.current_health = self.current_health + damage
        if (self.current_health <= 0):
            self.critical_injurys[self.current_health*(-1)] = True
        if (self.current_health < -2):
            self.current_health = -2
        elif (self.current_health > self.max_health):
            self.current_health = self.max_health


if __name__ == ("__main__"):
    characteristics_0 = {'S': 25, 'A': 25, 'T': 25, 'P': 25, 'I': 25, 'WP': 25, 'C': 25}
    skills_0 = {"melee_strength": 10, "melee_agility": 10, "shield": 15, "parry": 15, "dodge": -20}
    talents_0 = set(["quick_strike", "battle dance"])
    equipment_0 = {'H': 'none',
                 'B': 'none',
                 'L': 'none',
                 'LA': 'none',
                 'RA': 'none'}
    test_charatcer = Character(characteristics_0, skills_0, talents_0, equipment_0)



