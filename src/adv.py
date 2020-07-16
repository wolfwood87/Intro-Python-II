from roominstances import roomi
from roominstances import room_list
from player import Player
import random
# Declare all the rooms


print(room_list)
# Link rooms together
random.shuffle(room_list["ground"])
print(room_list)
random.shuffle(room_list["upper"])
random.shuffle(room_list["basement"])
roomi["hall"].n_to = roomi["foyer"]
roomi["hall"].e_to = roomi[room_list["ground"][0]]
roomi["hall"].w_to = roomi[room_list["ground"][3]]
roomi[room_list["ground"][3]].e_to = roomi["hall"]
roomi[room_list["ground"][0]].w_to = roomi["hall"]
roomi[room_list["ground"][0]].n_to = roomi[room_list["ground"][1]]
roomi[room_list["ground"][0]].e_to = roomi[room_list["ground"][2]]
roomi[room_list["ground"][1]].s_to = roomi[room_list["ground"][0]]
roomi[room_list["ground"][1]].w_to = roomi["foyer"]
roomi[room_list["ground"][2]].w_to = roomi[room_list["ground"][0]]
roomi["foyer"].n_to = roomi["stair"]
roomi["foyer"].s_to = roomi["hall"]
roomi["foyer"].w_to = roomi[room_list["ground"][4]]
roomi[room_list["ground"][3]].n_to = roomi[room_list["ground"][4]]
roomi[room_list["ground"][4]].s_to = roomi[room_list["ground"][3]]
roomi[room_list["ground"][4]].w_to = roomi[room_list["ground"][5]]
roomi[room_list["ground"][5]].e_to = roomi[room_list["ground"][4]]
roomi[room_list["ground"][4]].n_to = roomi[room_list["ground"][6]]
roomi[room_list["ground"][6]].s_to = roomi[room_list["ground"][4]]
roomi[room_list["ground"][5]].n_to = roomi[room_list["ground"][7]]
roomi[room_list["ground"][7]].s_to = roomi[room_list["ground"][5]]
roomi[room_list["ground"][7]].e_to = roomi[room_list["ground"][6]]
roomi["stair"].n_to = roomi["upper"]
roomi["upper"].n_to = roomi["stair"]
roomi["upper"].w_to = roomi[room_list["upper"][0]]
roomi["upper"].s_to = roomi[room_list["upper"][1]]
roomi[room_list["upper"][0]].e_to = roomi["upper"]
roomi[room_list["upper"][1]].n_to = roomi["hall"]
roomi[room_list["upper"][1]].w_to = roomi[room_list["upper"][2]]
roomi[room_list["upper"][0]].s_to = roomi[room_list["upper"][2]]
roomi[room_list["ground"][2]].e_to = roomi[room_list["ground"][1]]
roomi["stair"].s_to = roomi["foyer"]
roomi["stair"].e_to = roomi["basement"]
roomi["basement"].w_to = roomi["stair"]
roomi["basement"].e_to = roomi[room_list["basement"][0]]
roomi[room_list["basement"][0]].w_to = roomi["basement"]
roomi[room_list["basement"][0]].n_to = roomi[room_list["basement"][2]]
roomi[room_list["basement"][2]].s_to = roomi[room_list["basement"][0]]
roomi[room_list["basement"][0]].e_to = roomi[room_list["basement"][3]]
roomi[room_list["basement"][3]].w_to = roomi[room_list["basement"][0]]
roomi[room_list["basement"][3]].e_to = roomi[room_list["basement"][4]]
roomi[room_list["basement"][4]].w_to = roomi[room_list["basement"][3]]
roomi[room_list["basement"][2]].w_to = roomi[room_list["basement"][5]]
roomi[room_list["basement"][5]].w_to = roomi[room_list["basement"][2]]
roomi["basement"].s_to = roomi[room_list["basement"][1]]
roomi[room_list["basement"][1]].n_to = roomi["basement"]
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
diroutput = ""
directions = roomi[f"{gameplayer.room}"].get_directions()
for i in range(len(directions)):
    if(i == len(directions) - 1 and len(directions) >= 1):
        diroutput += f" and {directions[i]}."
    elif(i == len(directions) -1 and len(directions) == 0):
        diroutput += f" {directions[i]}."
    else:
        diroutput += f" {directions[i]}"

print(roomi[f"{gameplayer.room}"].description, f"You may explore rooms to the{diroutput}")
game = input("Please choose a direction to get started or select q to quit:\n")

while(game != "q"):
    if(game.lower() == "n"):
        if(roomi[f"{gameplayer.room}"].n_to == ""):
            print("There is nothing in that direction")
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].n_to
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description, f" You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "s"):
        if(roomi[f"{gameplayer.room}"].s_to == ""):
            print("There is nothing in that direction")
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].s_to
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description, f" You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "w"):
        if(roomi[f"{gameplayer.room}"].w_to == ""):
            print("There is nothing in that direction")
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].w_to
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description, f" You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
    elif(game.lower() == "e"):
        if(roomi[f"{gameplayer.room}"].e_to == ""):
            print("There is nothing in that direction")
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
        else:
            gameplayer.room = roomi[f"{gameplayer.room}"].e_to
            diroutput = ""
            directions = roomi[f"{gameplayer.room}"].get_directions()
            for i in range(len(directions)):
                if(i == len(directions) - 1 and len(directions) >= 1):
                    diroutput += f" and {directions[i]}."
                elif(i == len(directions) -1 and len(directions) == 0):
                    diroutput += f" {directions[i]}."
                else:
                    diroutput += f" {directions[i]}"
            print(f"You are currently in the {gameplayer.room}.")
            print(roomi[f"{gameplayer.room}"].description, f" You may explore rooms to the{diroutput}")
            game = input("Please choose a direction or select q to quit:\n")
    else:
        print("Invalid selection. Please choose a direction using n, s, e, w, or select q to quit")
        game = input("Please choose a direction or select q to quit:\n")
