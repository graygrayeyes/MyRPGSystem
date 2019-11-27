import math

min_human_char_value = 0
normal_human_char_value = 4
max_human_char_value = 12

class CharacteristicS:
    def __init__(self,
                 chars_values='not used var chars_values',
                 s=normal_human_char_value,
                 a=normal_human_char_value,
                 e=normal_human_char_value,
                 p=normal_human_char_value,
                 wp=normal_human_char_value,
                 i=normal_human_char_value,
                 c=normal_human_char_value):

        if chars_values == 'not used var chars_values':
            self.chars_values = {'S': s, # strength
                                 'A': a, # agility
                                 'E': e, # endurance
                                 'P': p, # perception
                                 'WP': wp, # will_power
                                 'I': i, # intelligence
                                 'C': c} # charisma
        else:
            self.chars_values = {'S': chars_values['S'],  # strength
                                 'A': chars_values['A'],  # agility
                                 'E': chars_values['E'],  # endurance
                                 'P': chars_values['P'],  # perception
                                 'WP': chars_values['WP'],  # will_power
                                 'I': chars_values['I'],  # intelligence
                                 'C': chars_values['C']}  # charisma

    def change_characteristic(self, char, added_value=0, set_value="not used var set_value"):
        self.chars_values[char] += added_value
        if set_value != "not used var set_value":
            self.chars_values[char] = set_value
        if self.chars_values[char] > max_human_char_value:
            self.chars_values[char] = max_human_char_value
        if self.chars_values[char] < min_human_char_value:
            self.chars_values[char] = min_human_char_value

    def get_characteristic_modifier(self, char_sign):
        if self.chars_values[char_sign] == 1:
            return 1
        else:
            return int(math.floor(self.chars_values[char_sign]/2)) # math.floor - rounding down

