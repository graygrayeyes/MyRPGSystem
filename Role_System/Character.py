from Common_Consts import *


class Character:
    def __init__(self, characteristics, skills, talents, equipment):
        # Set characteristics, skills, talents
        self.skills = Skills_Set(skills)
        self.talents = set()
        self.characteristics = {'S': characteristics['S'], # strength
                                'A': characteristics['A'], # agility
                                'T': characteristics['T'], # toughness
                                'P': characteristics['P'], # perception
                                'I': characteristics['I'], # intellect
                                'WP': characteristics['WP'], # will_power
                                'C': characteristics['C']} # charisma


        # for key, value in skills.items():
        #     self.skills[key] = value

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

    def compute_chr_bonus(self, chr_name):
        return int(self.characteristics[chr_name]/10)

class Health_Condition:
    def __init__(self, toughness_bonus, will_power_bonus):
        self.body = Body(toughness_bonus)
        self.cold_resistance = toughness_bonus
        self.poison_resistance = toughness_bonus
        self.mind_resistance = will_power_bonus

class Body:
    def __init__(self, toughness_bonus):
        head = Body_Part('H', toughness_bonus)
        left_arm = Body_Part('LA', toughness_bonus)
        right_arm = Body_Part('RA', toughness_bonus)
        torso = Body_Part('T', toughness_bonus)
        left_leg = Body_Part('LL', toughness_bonus)
        right_leg = Body_Part('RL', toughness_bonus)

        self.parts = {'H': head,
                      'LA': left_arm,
                      'RA': right_arm,
                      'T': torso,
                      'LL': left_leg,
                      'RL': right_leg}

    def update_body (self, toughness_bonus):
        for key in self.parts:
            self.parts[key].update_part_max_health(toughness_bonus)

    def get_hit_or_hill_all_body(self, damage):
        for key in self.parts:
            self.parts[key].get_hit_or_heal(damage)

class Body_Part:
    def __init__(self, type, toughness_bonus):
        self.type = type # 'H', 'LA', 'RA', 'T', 'LL', 'RL'
        self.max_health = self.compute_max_health(toughness_bonus)
        self.current_health = self.max_health
        self.critical_injurys = [False, False, False]

    def update_part_max_health(self, toughness_bonus):
        self.max_health = self.compute_max_health(toughness_bonus)
        self.current_health = self.max_health

    def compute_max_health(self, toughness_bonus):
        health_range_body = [4, 5, 6, 7, 8]
        health_range_other_parts = [3, 3, 4, 5, 6]
        if(self.type == 'T'):
            return health_range_body[toughness_bonus]
        else: # H, RA, LA, LL, RL
            return health_range_other_parts[toughness_bonus]

    def get_hit_or_heal(self, damage):
        self.current_health = self.current_health + damage
        if (self.current_health <= 0): # отметка о критической травме
            self.critical_injurys[self.current_health*(-1)] = True
        if (self.current_health < -2):
            self.current_health = -2
        elif (self.current_health > self.max_health):
            self.current_health = self.max_health


if __name__ == ("__main__"):
    characteristics_0 = {'S': 25, 'A': 25, 'T': 25, 'P': 25, 'I': 25, 'WP': 25, 'C': 25}
    skills_0 = {"melee_strength": 2,
                "unarmed": 1,
                "throwing": 2,

                "melee_agility": 2,
                "bow":1,
                "shield": 3,
                "parry": 3,
                "dodge": 0,

                "firearms": 0}
    talents_0 = set(["quick_strike",
                     "battle dance"])
    equipment_0 = {'H': 'none',
                 'B': 'none',
                 'L': 'none',
                 'LA': 'none',
                 'RA': 'none'}
    test_charatcer = Character(characteristics_0, skills_0, talents_0, equipment_0)



