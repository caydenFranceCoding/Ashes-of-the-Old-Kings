import knight_game
print(pygame.display)

game_world = {
    "entrance": {
        "name": "Entrance Hall",
        "description": "You enter into the Grand Hall of Cordithin. A giant heavy door leads north, and a dimly lit corridor goes east. ",
        "exits": {"north": "great_hall", "east": "corridor"},
        "items": []
    },
    "great_hall": {
        "name": "Great Hall",
        "description": "A spacious hallway with high ceilings and chandeliers. On the walls, you see massive windows. When looking outside, you can see the vast wilderness surrounding you with trees.",
        "exits": {"south": "entrance"},
        "items": []
    },
    "corridor": {
        "name": "Dimly Lit Corridor",
        "description": "A narrow passage with flickering torches. You can go west.",
        "exits": {"west": "entrance"},
        "items": ["torch"]
    }
}

current_location = "entrance"

def display_location(location):
    """Prints the name and the description of the current location."""
    print(f"\n--- {game_world[location]['name']}---")
    if game_world[location]['items']:
        print("Items here:", ", ".join(game_world[location]['items']))
    if game_world[location]['exits']:
        print("Exits:", ", ".join(game_world[location]['exits'].keys()))

while True:
    display_location(current_location)
    command = input("\nWhat do you want to do? ").lower()
    if command in ["north", "south", "east", "west"]:
        if command in game_world[current_location]['exits']:
            next_location = game_world[current_location]['exits'][command]
            current_location = next_location
        else:
            print("You may not go that way.")
    elif command == "quit":
        break
    else:
        print("Invalid command.")

print("thanks for playing!")