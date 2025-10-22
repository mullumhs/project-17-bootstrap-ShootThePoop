import random

cards = [
    {"Name" : "Archer Queen", "Rarity" : "Champion", "Elixir": 5},
    {"Name" : "Archers", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Arrows", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Baby Dragon", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Balloon", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Bandit", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Barbarian Barrel", "Rarity" : "Epic", "Elixir": 2},
    {"Name" : "Barbarian Hut", "Rarity" : "Rare", "Elixir": 6},
    {"Name" : "Barbarians", "Rarity" : "Common", "Elixir": 5},
    {"Name" : "Bats", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Battle Healer", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Battle Ram", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Berserker", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Bomb Tower", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Bomber", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Boss Bandit", "Rarity" : "Champion", "Elixir": 6},
    {"Name" : "Bowler", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Cannon", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Cannon Cart", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Clone", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Dark Prince", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Dart Goblin", "Rarity" : "Rare", "Elixir": 3},
    {"Name" : "Earthquake", "Rarity" : "Rare", "Elixir": 3},
    {"Name" : "Electro Dragon", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Electro Giant", "Rarity" : "Epic", "Elixir": 7},
    {"Name" : "Electro Spirit", "Rarity" : "Common", "Elixir": 1},
    {"Name" : "Electro Wizard", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Elite Barbarians", "Rarity" : "Common", "Elixir": 6},
    {"Name" : "Elixir Collector", "Rarity" : "Rare", "Elixir": 6},
    {"Name" : "Elixir Golem", "Rarity" : "Rare", "Elixir": 3},
    {"Name" : "Executioner", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Fire Spirit", "Rarity" : "Common", "Elixir": 1},
    {"Name" : "Fireball", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Firecracker", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Fisherman", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Flying Machine", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Freeze", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Furnace", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Giant", "Rarity" : "Rare", "Elixir": 5},
    {"Name" : "Giant Skeleton", "Rarity" : "Epic", "Elixir": 6},
    {"Name" : "Snowball", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Goblin Barrel", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Goblin Cage", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Goblin Demolisher", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Goblin Drill", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Goblin Gang", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Goblin Giant", "Rarity" : "Epic", "Elixir": 6},
    {"Name" : "Goblin Hut", "Rarity" : "Rare", "Elixir": 5},
    {"Name" : "Goblin Machine", "Rarity" : "Legendary", "Elixir": 5},
    {"Name" : "Goblins", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Goblinstein", "Rarity" : "Champion", "Elixir": 5},
    {"Name" : "Golden Knight", "Rarity" : "Champion", "Elixir": 4},
    {"Name" : "Golem", "Rarity" : "Epic", "Elixir": 8},
    {"Name" : "Graveyard", "Rarity" : "Legendary", "Elixir": 5},
    {"Name" : "Guards", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Heal Spirit", "Rarity" : "Rare", "Elixir": 1},
    {"Name" : "Hog Rider", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Hunter", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Ice Golem", "Rarity" : "Rare", "Elixir": 2},
    {"Name" : "Ice Spirit", "Rarity" : "Common", "Elixir": 1},
    {"Name" : "Ice Wizard", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Inferno Dragon", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Inferno Tower", "Rarity" : "Rare", "Elixir": 5},
    {"Name" : "Knight", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Lava Hound", "Rarity" : "Legendary", "Elixir": 7},
    {"Name" : "Lightning", "Rarity" : "Epic", "Elixir": 6},
    {"Name" : "Lumberjack", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Magic Archer", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Mega Knight", "Rarity" : "Legendary", "Elixir": 7},
    {"Name" : "Mega Minion", "Rarity" : "Rare", "Elixir": 3},
    {"Name" : "Mighty Miner", "Rarity" : "Champion", "Elixir": 4},
    {"Name" : "Miner", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Mini PEKKA", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Minion Horde", "Rarity" : "Common", "Elixir": 5},
    {"Name" : "Minions", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Mirror", "Rarity" : "Epic", "Elixir": 0},
    {"Name" : "Monk", "Rarity" : "Champion", "Elixir": 5},
    {"Name" : "Mortar", "Rarity" : "Common", "Elixir": 4},
    {"Name" : "Mother Witch", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Musketeer", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Night Witch", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "PEKKA", "Rarity" : "Epic", "Elixir": 7},
    {"Name" : "Phoenix", "Rarity" : "Legendary", "Elixir": 4},
    {"Name" : "Poison", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Prince", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Princess", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Goblin Curse", "Rarity" : "Epic", "Elixir": 2}, 
    {"Name" : "Little Prince", "Rarity" : "Champion", "Elixir": 3},
    {"Name" : "Rage", "Rarity" : "Epic", "Elixir": 2},
    {"Name" : "Ram Rider", "Rarity" : "Legendary", "Elixir": 5},
    {"Name" : "Rascals", "Rarity" : "Common", "Elixir": 5},
    {"Name" : "Rocket", "Rarity" : "Rare", "Elixir": 6},
    {"Name" : "Royal Delivery", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Royal Ghost", "Rarity" : "Legendary", "Elixir": 3},
    {"Name" : "Royal Giant", "Rarity" : "Common", "Elixir": 6},
    {"Name" : "Royal Hogs", "Rarity" : "Rare", "Elixir": 5},
    {"Name" : "Royal Recruits", "Rarity" : "Common", "Elixir": 7},
    {"Name" : "Rune Giant", "Rarity" : "Epic", "Elixir": 4},
    {"Name" : "Skeleton Army", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Skeleton Barrel", "Rarity" : "Common", "Elixir": 3},
    {"Name" : "Skeleton Dragons", "Rarity" : "Common", "Elixir": 4},
    {"Name" : "Skeleton King", "Rarity" : "Champion", "Elixir": 4},
    {"Name" : "Skeletons", "Rarity" : "Common", "Elixir": 1},
    {"Name" : "Sparky", "Rarity" : "Legendary", "Elixir": 6},
    {"Name" : "Spear Goblins", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Spirit Empress", "Rarity" : "Legendary", "Elixir": 0},
    {"Name" : "Suspicious Bush", "Rarity" : "Rare", "Elixir": 2},
    {"Name" : "Tesla", "Rarity" : "Common", "Elixir": 4},
    {"Name" : "Log", "Rarity" : "Legendary", "Elixir": 2},
    {"Name" : "Three Musketeers", "Rarity" : "Rare", "Elixir": 9},
    {"Name" : "Tombstone", "Rarity" : "Rare", "Elixir": 3},
    {"Name" : "Tornado", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Valkyrie", "Rarity" : "Rare", "Elixir": 4},
    {"Name" : "Void", "Rarity" : "Epic", "Elixir": 3},
    {"Name" : "Wall Breakers", "Rarity" : "Epic", "Elixir": 2},
    {"Name" : "Witch", "Rarity" : "Epic", "Elixir": 5},
    {"Name" : "Wizard", "Rarity" : "Rare", "Elixir": 5},
    {"Name" : "X-Bow", "Rarity" : "Epic", "Elixir": 6},
    {"Name" : "Zap", "Rarity" : "Common", "Elixir": 2},
    {"Name" : "Zappies", "Rarity" : "Rare", "Elixir": 4},
]

def get_number(prompt, min=None, max=None):
    while True:
        try:
            number = int(input(prompt))  # Convert input to integer

            # If min is specified, ensure number is greater or equal
            if min is not None and number < min:
                print(f"Please enter a number between {min} and {max}.")
                continue

            # If max is specified, ensure number is less or equal
            if max is not None and number > max:
                print(f"Please enter a number between {min} and {max}.")
                continue

            return number  # Return valid number
        except ValueError:
            print(f"Invalid input. Please enter a whole number between {min} and {max}")


def hints():
    print("Would you like to be given:")
    print("1. Card rarity")
    print("2. Elixir cost")
    print("3. Both")
    choice = get_number("Make your choice: ", 1, 3)

    if choice == 1: #Rarity hint
        random_card = random.choice(cards)
        print(f"One of your remaining cards rarities is: {random_card['Rarity']}.")
        #hints_used += 1

    
    elif choice == 2: #Elixir hint
        random_card = random.choice(cards)
        print(f"One of your remaining cards elixir cost is: {random_card['Elixir']}.")
        #hints_used += 1

    elif choice == 3: #Both hint
        random_card = random.choice(cards)
        print(f"One of your remaining cards rarity is {random_card['Rarity']} with elixir cost {random_card['Elixir']}.")
        #hints_used += 2


    ### add another hint that gives the first letter of the card

def display_guessed():
    print("Cards already guessed:")
    if len(guessed_cards) == 0:
        print("No cards guessed.")
    else:
        for i, card in enumerate(guessed_cards, 1):
            print(f"{i}. {card['Name']} - {card['Rarity']} - {card['Elixir']} Elixir")
        input("Press enter to return to the game.")

guessed_cards = []
#hints_used = 0
print("\n\n\nWelcome to the clash royale card game. ")
print("Press 1 at any time to view all cards that you have already guessed.")
print("Press 2 at any time for a hint")
print("You may now begin.")

while len(cards) > 1:
    guess = input("").title()
    if guess == "1":
        display_guessed()

    elif guess == "2":
        hints()

    matched_card = None
    for card in cards:
        if card["Name"].lower() == guess.lower():
            matched_card = card
            break

    if matched_card:
        cards.remove(matched_card)
        guessed_cards.append(matched_card)
        print(f"{matched_card['Name']} was guessed correctly! {len(cards)-1} remaining.")
    else:
        print("Card does not exist or has already been guessed.")

    
print("You beat the game!")