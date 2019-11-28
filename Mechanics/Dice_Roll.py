import random as rnd

def d20_roll():
    rnd.seed()
    return rnd.randint(1, 20)
