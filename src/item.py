from card import Card

class Item(Card):
    def __init__(self, name, description, modifier, stat_modified, equipped = "false"):
        super().__init__(name, description)
        self.modifier = modifier
        self.stat_modified = stat_modified
        self.equipped = equipped
    def __str__(self):
        return f"""{self.name}\n{self.description}"""
    def on_take(self):
        return f"You have picked up {self.name}"
    def on_equip(self, player, stats):
        stat = 0
        for i in stats.keys():
            if(i == self.stat_modified):
                stats[i] = stats[i] + self.modifier
                stat = stats[i]
        self.equipped = "true"
        return f"You have equipped {self.name}. Your {self.stat_modified} is now {stat}", stat, self.stat_modified
    def on_unequip(self, player, stats):
        stat = 0
        for i in stats.keys():
            if(i == self.stat_modified):
                stats[i] = stats[i] - self.modifier
                stat = stats[i]
        self.equipped = "false"
        return f"You have unequipped {self.name}. Your {self.stat_modified} is now {stat}", stat, self.stat_modified
    def on_drop(self):
        return f"You have dropped {self.name}"
