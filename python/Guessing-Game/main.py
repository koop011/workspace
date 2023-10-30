# Guessing Game
# Ask the user to guess a random number between a randomized range.

def game_mode():
    game_mode_selection_message = """
    Choose your game mode:
    -Number Only-
    [1] Simple
    [2] Randomized
    """
    
    print(game_mode_selection_message)
    
    game_mode = input("Game mode: ")
    return game_mode

def get_random_number():
    pass

def main():
    welcome_message = """
    ----- Guess a Number -----
    Welcome to the guessing world where you'll be guessing various things.
    For starts, let's guess a number!
    """

    print(welcome_message)

    game_type = game_mode()
    
    match (int(game_type)):
        case 1:
            print("testing")

if __name__ == "__main__":
    main()

