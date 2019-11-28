

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
        self.current_health = self.current_health - damage
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


endurance_hp_offset = 0
mind_hp_offset = 0


class Health_Condition:
    def __init__(self, endurance_modifier, will_power_modifier):
        self.body = Body(endurance_modifier)

        self.max_endurance_hp = endurance_modifier + endurance_hp_offset
        self.max_mind_hp = will_power_modifier + mind_hp_offset

        self.hp_types = {'bleed_hp': endurance_modifier,
                         'cold_hp': endurance_modifier,
                         'poison_hp': endurance_modifier,
                         'mind_hp': will_power_modifier}

    def update_endurance_hp(self, endurance_modifier):
        self.max_endurance_hp = endurance_modifier + endurance_hp_offset
        self.hp_types = {'bleed_hp': endurance_modifier,
                         'cold_hp': endurance_modifier,
                         'poison_hp': endurance_modifier,
                         'mind_hp':  self.max_mind_hp}

    def update_mind_hp(self, will_power_modifier):
        self.max_mind_hp = will_power_modifier + mind_hp_offset
        self.hp_types['mind_hp'] = self.max_mind_hp

    def other_hp_hit_or_heal(self, damage, hp_type):
        if(hp_type == 'mind_hp'):
            self.hp_types[hp_type] = self.hp_types[hp_type] - damage
            if (self.hp_types[hp_type] < 0):
                self.hp_types[hp_type] = 0
            elif self.hp_types[hp_type] > self.max_mind_hp:
                self.hp_types[hp_type] = self.max_mind_hp
        else: # bleed_hp, cold_hp, poison_hp
            self.hp_types[hp_type] = self.hp_types[hp_type] - damage
            if (self.hp_types[hp_type] < 0):
                self.hp_types[hp_type] = 0
            elif self.hp_types[hp_type] > self.max_endurance_hp:
                self.hp_types[hp_type] = self.max_endurance_hp






