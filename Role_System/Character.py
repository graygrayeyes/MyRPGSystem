from Characteristics import *
from Skills import *
from Specializations import *
from Traits import *

from Health import *

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

if __name__ == '__main__':
    test_character = Character('Marvin')
    print('end')