

class Body_Part:
    def __init__(self, type, endurance_modifier):
        self.type = type # 'H', 'LA', 'RA', 'T', 'LL', 'RL'
        self.max_health = self.compute_max_health(endurance_modifier)
        self.current_health = self.max_health

    def update_part_max_health(self, endurance_modifier):
        self.max_health = self.compute_max_health(endurance_modifier)
        self.current_health = self.max_health

    def compute_max_health(self, endurance_modifier):
        if self.type == 'T': # torso
            if endurance_modifier <= 3:
                return endurance_modifier + 2
            else: # toughness_bonus >=4
                return endurance_modifier + 3
        else:
            return endurance_modifier

    def get_hit_or_heal(self, damage):
        self.current_health = self.current_health + damage
        if (self.current_health < -2):
            self.current_health = -2
        elif (self.current_health > self.max_health):
            self.current_health = self.max_health


class Body:
    def __init__(self, endurance_modifier):
        self.parts = {'H': Body_Part('H', endurance_modifier),
                      'LA': Body_Part('LA', endurance_modifier),
                      'RA': Body_Part('RA', endurance_modifier),
                      'T': Body_Part('T', endurance_modifier),
                      'LL': Body_Part('LL', endurance_modifier),
                      'RL': Body_Part('RL', endurance_modifier)
                      }

    def update_body(self, endurance_modifier):
        for key in self.parts:
            self.parts[key].update_part_max_health(endurance_modifier)

    def get_hit_or_hill_at_part(self, damage, type):
        self.parts[type].get_hit_or_heal(damage)

    def get_hit_or_hill_all_body(self, damage):
        for key in self.parts:
            self.parts[key].get_hit_or_heal(damage)


class Health_Condition:
    def __init__(self, endurance_modifier, will_power_modifier):
        self.body = Body(endurance_modifier)
        self.cold_resistance = endurance_modifier
        self.poison_resistance = endurance_modifier
        self.mind_resistance = will_power_modifier


