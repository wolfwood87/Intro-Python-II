# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, might, max_might, speed, max_speed, sanity, max_sanity, knowledge, max_knowledge, allegiance = "hero", room = "hall", item_held = ""):
        self.name = name
        self.allegiance = allegiance
        self.might = might
        self.max_might = max_might
        self.speed = speed
        self.max_speed = max_speed
        self.sanity = sanity
        self.max_sanity = max_sanity
        self.knowledge = knowledge
        self.max_knowledge = max_knowledge
        self.item_held = item_held
        self.room = room
    def __str__(self):
        return f"""You have chosen {self.name}, a {self.allegiance}. Your stats are:
        Might: {self.might}/{self.max_might}
        Speed: {self.speed}/{self.max_speed}
        Sanity: {self.sanity}/{self.max_sanity}
        Knowledge: {self.knowledge}/{self.max_knowledge}       
        Your starting room is {self.room}\n"""
        