import math

min_human_char_value = 0
normal_human_char_value = 4
max_human_char_value = 12

normal_human_chars_values = {'S': normal_human_char_value, # strength
                             'A': normal_human_char_value, # agility
                             'E': normal_human_char_value, # endurance
                             'P': normal_human_char_value, # perception
                             'WP': normal_human_char_value, # will_power
                             'I': normal_human_char_value, # intelligence
                             'C': normal_human_char_value} # charisma

class CharacteristicS:
    def __init__(self, chars_values='not used var chars_values'):
        if chars_values == 'not used var chars_values':
            self.chars_values = normal_human_chars_values
        else:
            self.chars_values = chars_values

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

