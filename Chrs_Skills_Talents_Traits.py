min_human_char_value = 0
normal_human_char_value = 5
max_human_char_value = 12

class CharacteristicS:
    def __init__(self,
                 s=normal_human_char_value,
                 a=normal_human_char_value,
                 t=normal_human_char_value,
                 p=normal_human_char_value,
                 wp=normal_human_char_value,
                 i=normal_human_char_value,
                 c=normal_human_char_value):

        self.chars_values = {'S': s, 'A': a, 'T': t, 'P': p, 'WP': wp, 'I': i, 'C': c}

    def change_characteristic(self, char, added_value=0, set_value="not used var set_value"):
        self.chars_values[char] += added_value
        if set_value != "not used var set_value":
            self.chars_values[char] = set_value
        if self.chars_values[char] > max_human_char_value:
            self.chars_values[char] = max_human_char_value
        if self.chars_values[char] < min_human_char_value:
            self.chars_values[char] = min_human_char_value

basic_skill_offset = 0
advanced_skill_offset = 1
min_human_skill_tr_level = -1
max_human_basic_skill_tr_level = 6
max_human_advanced_skill_tr_level = max_human_basic_skill_tr_level + (advanced_skill_offset - basic_skill_offset)


class Skill:
    def __init__(self, name, char, training_level=min_human_skill_tr_level,
                 advanced=False, dual_charS=False, second_char = "not used var second_char"):
        self.name = name
        self.char = char
        self.dual_charS = dual_charS
        if self.dual_charS == True:
            self.second_char = second_char
        self.training_level = training_level
        self.advanced = advanced

    def get_modifier(self):
        if self.advanced == True:
            if self.training_level <= -1:
                return "Can't use advanced skill with training_level < 1"
            elif self.training_level >= 0:
                return self.training_level - advanced_skill_offset
        else: # basic skill
            if self.training_level <= -1:
                return -4
            elif self.training_level >= 0:
                return self.training_level - basic_skill_offset

    def change_skill(self, added_tr_level=0, set_tr_level="not used var set_tr_level"):
        self.training_level += added_tr_level
        if set_tr_level != "not used var set_tr_level":
            self.training_level = set_tr_level

        if self.advanced == True:
            if self.training_level > max_human_advanced_skill_tr_level:
                self.training_level = max_human_advanced_skill_tr_level
        else: # basic skill
            if self.training_level > max_human_basic_skill_tr_level:
                self.training_level = max_human_basic_skill_tr_level

        if self.training_level < min_human_skill_tr_level:
            self.training_level = min_human_skill_tr_level

class SkillS_Set:
    def __init__(self, external_tr_lvls_by_names = "There isn't external_tr_lvls_by_names"):
        self.no_training_human_tr_lvls = {
            'strong_hit': -1, # all melee weapons except rapier
            'accuracy_hit': -1, # dagger, throwing knives, one-handed sword, two-handed sword, spear, halberd

            'dodge': -1,
            'parry': -1,
            'shield': -1,

            'throwing': -1,  # throwing knives, throwing axes, javelins
            'ballistics': -1, # sling, bow, crossbow
            'firearm': -1, # pistol, gun, rifle

            'alchemy': -1,
            'mechanisms': -1,
            'blacksmithing': -1,
            'medicine': -1,
            'acting art': -1,
            'trading': -1,
            'magic craft': -1
        }

        if external_tr_lvls_by_names == "There isn't external_tr_lvls_by_names":
            tr_lvls_by_names = self.no_training_human_tr_lvls
        else:
            tr_lvls_by_names = external_tr_lvls_by_names

        self.skills = {
            "strong_hit": Skill(name="strong_hit", char="S", training_level=tr_lvls_by_names['strong_hit']),
            "accuracy_hit": Skill(name="accuracy_hit", char="A", training_level=tr_lvls_by_names['accuracy_hit'],
                                  advanced=True),

            'dodge': Skill(name="dodge", char="A", training_level=tr_lvls_by_names['dodge']),
            'parry': Skill(name="parry", char="A", training_level=tr_lvls_by_names['parry']),
            'shield': Skill(name="shield", char="A", training_level=tr_lvls_by_names['shield']),

            'throwing': Skill(name="throwing", char="S", training_level=tr_lvls_by_names['throwing']),
                # throwing knives, throwing axes, javelins, bombs, stones
            'ballistics': Skill(name="ballistics", char="A", training_level=tr_lvls_by_names['ballistics']),
                # sling, bow, crossbow
            'firearm': Skill(name="firearm", char="P", training_level=tr_lvls_by_names['firearm'], advanced=True),
                # pistol, gun, rifle

            'alchemy': Skill(name="alchemy", char="I", training_level=tr_lvls_by_names['alchemy'], advanced=True),
            'mechanisms': Skill(name="mechanisms", char='I', training_level=tr_lvls_by_names['mechanisms'],
                                advanced=True, dual_charS=True, second_char = 'A'),
            'blacksmithing': Skill(name="blacksmithing", char='I', training_level=tr_lvls_by_names['blacksmithing'],
                                   advanced=True, dual_charS=True, second_char = 'S'),
            'medicine': Skill(name="medicine", char='I', training_level=tr_lvls_by_names['medicine'],
                                   advanced=True, dual_charS=True, second_char = 'P'),
            'magic craft': Skill(name="magic_craft", char='I', training_level=tr_lvls_by_names['magic_craft'],
                                   advanced=True, dual_charS=True, second_char = 'WP'),
            'trading': Skill(name="trading", char='I', training_level=tr_lvls_by_names['trading'],
                                   advanced=True, dual_charS=True, second_char = 'C'),
            'acting': Skill(name="acting", char='C', training_level=tr_lvls_by_names['acting']),
        }

'''
****** before d20 ******


skills_by_chrs = {
    "melee_strength": "S",
    "unarmed": "S",
    "throwing": "S",

    "melee_agility": "A",
    "shield": "A",
    "parry": "A",
    "dodge": "A",
    "bow": "A",

    "firearms": "P"
}

basic_skills = set(["melee_strength", "unarmed", "throwing", "shield", "parry", "dodge",])
advanced_skills = set(["melee_agility", "bow", "firearms", ])

class Skill:
    def __init__(self, advanced, chr, init_knowledge_level, name='name'):
        # self.name = name # название навыка ??? возможно без этого
        self.chr = chr  # характеристика, на которой базируется навык
        self.advanced = advanced # продвинутый скил нельзя использовать knowledge_level < 1
        self.knowledge_level = 0 # 0..4 - уровень навыка, (-20/нельзя использовать, 0, +5 .. +20)
        self.change_knowledge_level(init_knowledge_level)

    # def check_name(self, name):
    #     return self.name == name

    def change_knowledge_level(self, value):
        self.knowledge_level = self.knowledge_level + value
        if self.knowledge_level < 0:
            self.knowledge_level = 0
        elif self.knowledge_level > 5:
            self.knowledge_level = 5

    def compute_bonus_from_level(self):
        if self.knowledge_level == 0:
            if self.advanced == False:
                return -20
            else:
                return "Not available use"
        elif self.knowledge_level >= 1:
            return (self.knowledge_level-1)*5
        else:
            return "Not available knowledge level"

class Skills_Set:
    def __init__(self, skills_levels = 0):
        if(skills_levels==0):
            self.melee_strenght = Skill(advanced=False, chr='S', init_knowledge_level=0)
            self.unarmed = Skill(False, 'S', 0)
            self.throwing = Skill(False, 'S', 0)

            self.melee_agility = Skill(True, 'A', 0)
            self.shield = Skill(False, 'A', 0)
            self.parry = Skill(False, 'A', 0)
            self.dodge = Skill(False, 'A', 0)
            self.bow = Skill(True, 'A', 0)

            self.firearms = Skill(False, 'P', skills_levels['firearms'])
        else:
            self.melee_strenght = Skill(advanced=False, chr='S', init_knowledge_level=skills_levels['melee_strength'])
            self.unarmed = Skill(False, 'S', skills_levels['unarmed'])
            self.throwing = Skill(False, 'S', skills_levels['throwing'])

            self.melee_agility = Skill(True, 'A', skills_levels['melee_agility'])
            self.shield = Skill(False, 'A', skills_levels['throwing'])
            self.parry = Skill(False, 'A', skills_levels['parry'])
            self.dodge = Skill(False, 'A', skills_levels['dodge'])
            self.bow = Skill(True, 'A', skills_levels['bow'])

            self.firearms = Skill(False, 'P', skills_levels['firearms'])
'''
