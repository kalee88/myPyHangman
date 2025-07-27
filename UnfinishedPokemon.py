import random

# List of Pokémon (can add more)
pokemon_list = [
    {"name": "Pikachu", "type": "Electric"},
    {"name": "Charmander", "type": "Fire"},
    {"name": "Squirtle", "type": "Water"},
    {"name": "Bulbasaur", "type": "Grass/Poison"},
    {"name": "Jigglypuff", "type": "Normal/Fairy"},
    {"name": "Eevee", "type": "Normal"},
    {"name": "Snorlax", "type": "Normal"},
    {"name": "Gengar", "type": "Ghost/Poison"},
    {"name": "Machop", "type": "Fighting"},
    {"name": "Psyduck", "type": "Water"}
]

def play_game():
    print("🎮 Welcome to the Pokémon Guessing Game!")
    #Task .5 :  Get a random value from the dictionary!
    selected = 
    #Task 1 : Create 4 variables : name, type(pokemon's type), first_letter(First letter of pokemon's name), length(Represents the amount of letters in the pokemon's name). 
    #HINT : Use the dictionary to get the name and type.
    
    # Task 2 : Complete the following print statements with the correct variables
    print("\n🧩 Guess the Pokémon!")
    print(f"Hint 1: It has {} letters.")
    print(f"Hint 2: It starts with '{}'.")
    print(f"Hint 3: Its type is {}.")

    # Task 3 : Give the user 3 tries to guess the pokemon!
    attempts = 0
    #Complete the while loop
    while :
        #Complete the variable guess
        guess = 
        attempts += 1
        #Complete the if statement
        if :
            print(f"✅ Correct! It was {name}. You guessed it in {attempts} attempts.")
            break
        else:
            print("❌ Nope! Try again.")

# Start the game
play_game()
