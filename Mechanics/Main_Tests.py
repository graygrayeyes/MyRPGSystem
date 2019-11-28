from Dice_Roll import *
from math import *


def do_main_test(skill_val, difficult_modifier=0):
    d20_roll_result = d20_roll()
    delta = skill_val + difficult_modifier - d20_roll_result
    return [delta, d20_roll_result]


def do_opposed_test(skill_val_1, skill_val_2, difficult_modifier_1=0, difficult_modifier_2=0):
    result_1 = do_main_test(skill_val_1, difficult_modifier_1)
    result_2 = do_main_test(skill_val_2, difficult_modifier_2)
    opposed_delta = result_1[0] - result_2[0]
    return [opposed_delta, result_1[0], result_1[1], result_2[0], result_2[1]]

def do_hidden_attack_test(attack_skill_val_A, perception_val_D, difficult_modifier_A=0, difficult_modifier_D=0):
    if do_main_test(perception_val_D, difficult_modifier_D) >= 0:
        return 'attack was detected'
    else:
        return do_main_test(attack_skill_val_A, difficult_modifier_A)


def do_attack_opposed_test(skill_val_1, skill_val_2, difficult_modifier_1=0, difficult_modifier_2=0):
    result = do_opposed_test(skill_val_1, skill_val_2, difficult_modifier_1, difficult_modifier_2)

