import random as rnd

def d20_roll():
    rnd.seed()
    return rnd.randint(1, 20)



'''
def d100_roll():
    rnd.seed()
    return rnd.randint(1, 100)

def d10_roll():
    rnd.seed()
    return rnd.randint(1, 10)

def d5_roll():
    rnd.seed()
    return rnd.randint(1, 5)

if __name__ == ("__main__"):
    # for i in range(100):
    #     print(d100_roll())
    print()
    for i in range(100):
        print(d10_roll())
'''