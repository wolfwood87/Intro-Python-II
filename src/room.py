# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, key, name, description, marker = "", n_to = "", s_to = "", e_to = "", w_to = ""):
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
