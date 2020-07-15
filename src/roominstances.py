from room import Room

roomi = {
    'hall':  Room("hall", "Entrance Hall",
                  "North of you, the cave mount beckons"),

    'game':    Room("game", "Game Room", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'foyer': Room("foyer", "Foyer", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'stair': Room("stair", "Grand Staircase", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'library': Room("library", "Library", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'char': Room("char", "Charred Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'patio': Room("patio", "Patio", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'dining': Room("dining", "Dining Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'dust': Room("dust", "Dusty Hallway", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'abandoned': Room("abandoned", "Abandoned Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'kitchen': Room("kitchen", "Kitchen", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'upper': Room("upper", "Upper Landing", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'bloody': Room("bloody", "Bloody Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'statu': Room("statu", "Statuary Corridor", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'conserve': Room("conserve", "Conservatory", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'basement': Room("basement", "Basement Landing", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'organ': Room("organ", "Organ Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'creak': Room("creak", "Creaky Hallway", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'lab': Room("lab", "Research Laboratory", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'junk': Room("junk", "Junk Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'lard': Room("lard", "Larder", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'lake': Room("lake", "Underground Lake", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'furnace': Room("furnace", "Furnace Room", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room_list = {
    "ground": ["hall", "foyer", "stair", "game", "library", "char", "patio", "dining", "dust", "abandoned", "kitchen"
    ],
    "basement": ["basement", "organ", "creak", "lab", "lard", "lake", "furnace"],
    "upper": ["upper", "bloody", "statu", "conserve"]
}