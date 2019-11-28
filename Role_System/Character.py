from Characteristics import *
from Skills import *
from Specializations import *
from Traits import *

from Health import *

from Main_Tests import *

class Character:
    def __init__(self, name, chars_values='not used var chars_values',
                 skills_value='not used var skills_value'):
        self.name = name
        if chars_values == 'not used var chars_values':
            self.chars = CharacteristicS()
        else:
            self.chars = CharacteristicS(chars_values=chars_values)
        if skills_value == 'not used var skills_value':
            self.skills_set = SkillS_Set()
        else:
            self.skills_set = SkillS_Set(external_tr_lvls_by_names=skills_value)
        self.health_condition = Health_Condition(endurance_modifier=self.chars.get_characteristic_modifier('E'),
                                                will_power_modifier=self.chars.get_characteristic_modifier('WP'))

    def use_skill(self, name, difficult_modifier):
        result = do_main_test(self.skills_set.skills[name].get_modifier()
                              + self.chars.chars_values[self.skills_set.skills[name].char],
                              difficult_modifier)
        print(result)

if __name__ == '__main__':
    test_character = Character('Marvin', {'S': 5, 'A': 6, 'E': 5, 'P': 6, 'I': 7, 'WP': 4, 'C': 5}, {'strong_hit': 0})
    test_character.health_condition.other_hp_hit_or_heal(-3, 'poison_hp')
    test_character.use_skill('strong_hit', 0)
    print('end')