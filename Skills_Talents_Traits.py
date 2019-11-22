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