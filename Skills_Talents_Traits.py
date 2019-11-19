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
    def __init__(self, name, init_knowledge_level, advanced, chr):
        self.name = name # название навыка ??? возможно без этого
        self.chr = chr  # характеристика, на которой базируется навык
        self.advanced = advanced # продвинутый скил нельзя использовать knowledge_level < 1
        self.knowledge_level = 0 # 0..4 - уровень навыка, (-20/нельзя использовать, 0, +5 .. +20)
        self.change_knowledge_level(init_knowledge_level)


    def check_name(self, name):
        return self.name == name

    def change_knowledge_level(self, value):
        self.knowledge_level = self.knowledge_level + value
        if (self.knowledge_level < 0):
            self.knowledge_level = 0
        elif (self.knowledge_level > 4):
            self.knowledge_level = 4
