from roominstances import roomi
from roominstances import room_list
from player import Player
import random
# Declare all the rooms


print(room_list)
# Link rooms together
roomground = random.randint(1, len(room_list["ground"])-1)
roomup = random.randint(1, len(room_list["upper"])-1)
roombase = random.randint(1, len(room_list["basement"])-1)
roomi["hall"].n_to = roomi["foyer"]
roomi["foyer"].n_to = roomi["stair"]
roomi["foyer"].s_to = roomi["hall"]
roomi["stair"].n_to = roomi["upper"]
roomi["stair"].s_to = roomi["foyer"]
roomi["stair"].e_to = roomi["basement"]
roomi["basement"].w_to = roomi["stair"]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = [
    Player("Professor Longfellow", 3, 6, 4, 6, 3, 7, 5, 8),
    Player("Darrin 'Flash' Williams", 3, 7, 6, 8, 3, 7, 3, 7),
    Player("Heather Granville", 3, 8, 4, 8, 3, 6, 5, 8, "traitor"),
    Player("Madame Zostra", 4, 6, 3, 7, 4, 8, 4, 6),
    Player("Missy Dubourde", 3, 7, 5, 7, 3, 7, 4, 6),
]

output = ""
i = 1
for p in player:
    output += f"\n{i}. {p.name}"
    i += 1

selection = int(input(f"""Your starting player options are:{output}\n
Select a player:
"""))

try:
    gameplayer = player[selection - 1]
    print(gameplayer)
except:
    print("Incorrect selection.\n")
    selection = input(f"""Your starting player options are:{output}\n
Select a player:""")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"You are currently in the {gameplayer.room}.")
print(roomi[f"{gameplayer.room}"].description)
game = input("Please choose a direction to get started or select q to quit:\n")

while(game != "q"):
    if(game.lower() == "n"):
        if(roomi[f"{gameplayer.room}"].n_to == ""):
            if f"{gameplayer.room}" in room_list["ground"]:
                roomi[f"{gameplayer.room}"].n_to = roomi[room_list["ground"][roomground]]
                roomi[room_list["ground"][roomground]].s_to = roomi[f"{gameplayer.room}"]
                roomground = random.randint(1, len(room_list["ground"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].n_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["basement"]:
                roomi[f"{gameplayer.room}"].n_to = roomi[room_list["basement"][roombase]]
                roomi[room_list["basement"][roombase]].s_to = roomi[f"{gameplayer.room}"]
                roombase = random.randint(1, len(room_list["basement"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].n_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["upper"]:
                roomi[f"{gameplayer.room}"].n_to = roomi[room_list["upper"][roomup]]
                roomi[room_list["upper"][roomup]].s_to = roomi[f"{gameplayer.room}"]
                roomup = random.randint(1, len(room_list["upper"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].n_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            else:
                print("There is nothing in that direction")
                game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].n_to
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description)
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "s"):
        if(roomi[f"{gameplayer.room}"].s_to == ""):
            if gameplayer.room == "hall":
                print("Wolves are blocking the way outside. You can not leave.")
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["ground"]:
                roomi[f"{gameplayer.room}"].s_to = roomi[room_list["ground"][roomground]]
                roomi[room_list["ground"][roomground]].n_to = roomi[f"{gameplayer.room}"]
                roomground = random.randint(1, len(room_list["ground"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].s_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["basement"]:
                roomi[f"{gameplayer.room}"].s_to = roomi[room_list["basement"][roombase]]
                roomi[room_list["basement"][roombase]].n_to = roomi[f"{gameplayer.room}"]
                roombase = random.randint(1, len(room_list["basement"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].s_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["upper"]:
                roomi[f"{gameplayer.room}"].s_to = roomi[room_list["upper"][roomup]]
                roomi[room_list["upper"][roomup]].n_to = roomi[f"{gameplayer.room}"]
                roomup = random.randint(1, len(room_list["upper"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].s_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            else:
                print("There is nothing in that direction")
                game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].s_to
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description)
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "w"):
        if(roomi[f"{gameplayer.room}"].w_to == ""):
            if f"{gameplayer.room}" in room_list["ground"]:
                roomi[f"{gameplayer.room}"].w_to = roomi[room_list["ground"][roomground]]
                roomi[room_list["ground"][roomground]].e_to = roomi[f"{gameplayer.room}"]
                roomground = random.randint(1, len(room_list["ground"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].w_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["basement"]:
                roomi[f"{gameplayer.room}"].w_to = roomi[room_list["basement"][roombase]]
                roomi[room_list["basement"][roombase]].e_to = roomi[f"{gameplayer.room}"]
                roombase = random.randint(1, len(room_list["basement"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].w_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["upper"]:
                roomi[f"{gameplayer.room}"].w_to = roomi[room_list["upper"][roomup]]
                roomi[room_list["upper"][roomup]].e_to = roomi[f"{gameplayer.room}"]
                roomup = random.randint(1, len(room_list["upper"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].w_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            else:
                print("There is nothing in that direction")
                game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].w_to
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description)
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "e"):
        if(roomi[f"{gameplayer.room}"].e_to == ""):
            if f"{gameplayer.room}" in room_list["ground"]:
                roomi[f"{gameplayer.room}"].e_to = roomi[room_list["ground"][roomground]]
                roomi[room_list["ground"][roomground]].w_to = roomi[f"{gameplayer.room}"]
                roomground = random.randint(1, len(room_list["ground"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].e_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["basement"]:
                roomi[f"{gameplayer.room}"].e_to = roomi[room_list["basement"][roombase]]
                roomi[room_list["basement"][roombase]].w_to = roomi[f"{gameplayer.room}"]
                roombase = random.randint(1, len(room_list["basement"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].e_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            elif f"{gameplayer.room}" in room_list["upper"]:
                roomi[f"{gameplayer.room}"].e_to = roomi[room_list["upper"][roomup]]
                roomi[room_list["upper"][roomup]].w_to = roomi[f"{gameplayer.room}"]
                roomup = random.randint(1, len(room_list["upper"]))
                gameplayer.room = roomi[f"{gameplayer.room}"].e_to
                print(f"You are currently in the {gameplayer.room}.")
                print(roomi[f"{gameplayer.room}"].description)
                game = input("Please choose a direction or select q to quit:\n")
            else:
                print("There is nothing in that direction")
                game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].e_to
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description)
            game = input("Please choose a direction or select q to quit:\n")
    else:
        print("Invalid selection. Please choose a direction using n, s, e, w, or select q to quit")
        game = input("Please choose a direction or select q to quit:\n")
