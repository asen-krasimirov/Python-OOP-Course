

class Player:
    name: str
    hp: int
    mp: int
    skills: dict
    guild: str

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        player_information = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
            '\n'.join([f"==={skill_name} - {self.skills[skill_name]}" for skill_name in self.skills])
        ]
        if self.skills:
            player_information.append("")
        return '\n'.join(player_information)
