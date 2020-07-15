from card import Card

class Omen(Card):
    def __init__(self, name, description, modifier):
        super().__init__(name, description)
        self.modifier = modifier
    def __str__(self):
        return f"""{self.name}\n{self.description}"""
