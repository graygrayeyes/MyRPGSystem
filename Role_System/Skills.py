basic_skill_offset = 0
advanced_skill_offset = 1
min_human_skill_tr_level = -1
max_human_basic_skill_tr_level = 6
max_human_advanced_skill_tr_level = max_human_basic_skill_tr_level + (advanced_skill_offset - basic_skill_offset)

class Skill:
    def __init__(self, name, char, training_level=min_human_skill_tr_level,
                 advanced=False, secondary_char=False):
        self.name = name
        self.char = char
        self.secondary_char = secondary_char
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

no_training_human_tr_lvls = {
            'strong_hit': -1, 'accuracy_hit': -1,
            'dodge': -1, 'parry': -1, 'shield': -1,
            'throwing': -1, 'ballistics': -1, 'firearm': -1,

            'potions': -1, 'mechanisms': -1, 'blacksmithing': -1, 'healing': -1,
            'acting': -1, 'games': -1, 'commerce': -1, 'magic_craft': -1
        }

class SkillS_Set:
    def __init__(self, external_tr_lvls_by_names="There isn't external_tr_lvls_by_names"):
        tr_lvls_by_names = no_training_human_tr_lvls
        if external_tr_lvls_by_names != "There isn't external_tr_lvls_by_names":
            for i in external_tr_lvls_by_names.keys():
                tr_lvls_by_names[i] = external_tr_lvls_by_names[i]

        self.skills = {
            # ****** BATTLE skills ******
            "strong_hit": Skill(name="strong_hit", char="S", training_level=tr_lvls_by_names['strong_hit']),
                # all melee weapons except rapier
            "accuracy_hit": Skill(name="accuracy_hit", char="A", training_level=tr_lvls_by_names['accuracy_hit'],
                                  advanced=True),
            # dagger, throwing knives, one-handed sword, two-handed sword, spear, halberd

            'dodge': Skill(name="dodge", char="A", training_level=tr_lvls_by_names['dodge']),
                # 'dodge' skill has penalty to avoid distance atack -X; can't dodge firearm atack;
            'parry': Skill(name="parry", char="A", training_level=tr_lvls_by_names['parry']),
                # need weapon in hand; 'parry' skill has penalty to avoid distance atack -(X+Y);
                # can't parry firearm atack;
            'shield': Skill(name="shield", char="A", training_level=tr_lvls_by_names['shield']),
                # need shield in hand; 'shield' skill has NOT penalty to avoid distance atack;
                # can't block firearm atack;

            'throwing': Skill(name="throwing", char="S", training_level=tr_lvls_by_names['throwing']),
                # throwing knives, throwing axes, javelins, bombs, stones
            'ballistics': Skill(name="ballistics", char="A", training_level=tr_lvls_by_names['ballistics']),
                # sling, bow, crossbow
            'firearm': Skill(name="firearm", char="P", training_level=tr_lvls_by_names['firearm'], advanced=True),
                # pistol, gun, rifle

            # ****** MAGIC USING skills ******

            # ****** SOCIAL skills ******
            # C!
            # ****** SURVIVING skills ******
            # P! T! *(A, S)
            # plants_mushrooms:
            #
            # ****** ANIMAL skills ******
            # animal_care - C
            # animal_riding - A

            # ****** CRAFT and PROFESSIONAL skills ******
            'potions': Skill(name="potions", char="I", training_level=tr_lvls_by_names['potions'], advanced=True),
            'acting': Skill(name="acting", char='C', training_level=tr_lvls_by_names['acting']),

            'mechanisms': Skill(name="mechanisms", char='I', training_level=tr_lvls_by_names['mechanisms'],
                                advanced=True, secondary_char='A'),
            'blacksmithing': Skill(name="blacksmithing", char='I', training_level=tr_lvls_by_names['blacksmithing'],
                                   advanced=True, secondary_char='S'),
            'healing': Skill(name="healing", char='I', training_level=tr_lvls_by_names['healing'],
                             advanced=True, secondary_char='P'),
            'games': Skill(name="games", char='I', training_level=tr_lvls_by_names['games'],
                           advanced=True, secondary_char='P'),
            'commerce': Skill(name="commerce", char='C', training_level=tr_lvls_by_names['commerce'],
                              advanced=True, secondary_char='I'),
            'magic_craft': Skill(name="magic_craft", char='I', training_level=tr_lvls_by_names['magic_craft'],
                                 advanced=True, secondary_char='WP'), # Enchanting and Identify magic
            # IT WILL BE REALIZED BY SPELL in particular magic school -
            # Skill(name="divination", char='WP', training_level=tr_lvls_by_names['divination'],
            #                        advanced=True, dual_charS=True, second_char='P') # гадание
            # GO IN SCIENCE -
            # 'math_logic': Skill(name="math_logic", char="I",
            #       training_level=tr_lvls_by_names['math_logic'], advanced=True),

            # ****** KNOWLEDGES ******
            # language_(X): 3-4 present and 2-3 elders unusing now for magic; ALL advanced = True and char = I
            # basick_knowledge: only one; advanced = False and char = I;
            # science_knowledge: only one; advanced = True and char = I;
            #       There are Specializations for particular areas Specializations give bonus for appropriate
            #       science_knowledge tests and PROFESSIONAL skills (not ALL Specializations)
            #       * Specializations(bonus_for_skills):
            #       alchemy (potions), math_logic(commerce, games), physics(mechanisms, blacksmithing),
            #       biology(animal_care, plants_mushrooms), medicine(healing), linguistics(ALL language_X),
            #       philosophy, law,  history,
            # magic_knowledge: only one; advanced = True and char = I;
            #       There are Specializations by magic schools. They give ability to learn spells.
            #       Also there is Specialization "artifacts"  giving bonus to skill 'magic_craft'
            # religion_knowledge: only one; advanced = True and char = I;
            }