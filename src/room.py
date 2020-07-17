# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, key, name, description, marker = "", item_held = "", n_to = "", s_to = "", e_to = "", w_to = ""):
        self.key = key
        self.name = name
        self.description = description
        self.marker = marker
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __str__(self):
        return self.key
    def get_directions(self):
        output = []
        if(self.n_to != ""):
            output.append("north")
        if(self.s_to != ""):
            output.append("south")
        if(self.w_to != ""):
            output.append("west")
        if(self.e_to != ""):
            output.append("east")
        return output