from card import Card
import random
class Event(Card):
    def __init__(self, name, description, modifier, stat_modified):
        super().__init__(name, description)
        self.modifier = modifier
        self.stat_modified = stat_modified
    def __str__(self):
        return f"""{self.name}\n{self.description}"""
    def call_event(self, stat):
        roll = random.randint(1,7)
        success = "Rolling...\n", self.modifier, f"Congratulations. You have passed the trial."
        fail = "Rolling...\n", -self.modifier, f"So sorry. Better luck next time."
        if(roll > 3):
            return success
        else:
            return fail