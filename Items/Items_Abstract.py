class Item:
    def __init__(self, name, weight=1, worth=0, small=True):
        self.name = name
        self.weight = weight
        self.worh = worth
        self.small = small

class Container(Item): # позволяет носить size вещей типа small
    def __init__(self, name, weight=1, worth=0, size=1):
        Item.__init__(self, name, weight, worth, False)
        self.max_size = size

# ***** Certain weapon classes. Throwing_Weapon ******

# ***** Certain weapon classes. Range_Weapon ******


