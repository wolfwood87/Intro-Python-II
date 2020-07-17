from card import Card

class Omen(Card):
    def __init__(self, name, description, modifier, stat_modified):
        super().__init__(name, description)
        self.modifier = modifier
        self.stat_modified = stat_modified
    def __str__(self):
        return f"""{self.name}\n{self.description}"""
    def on_take(self):
        return f"You have picked up {self.name}", self.modifier, self.stat_modified
    def on_drop(self):
        return f"You have dropped {self.name}", -self.modifier, self.stat_modified
