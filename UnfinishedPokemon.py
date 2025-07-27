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
    selected = random.choice(pokemon_list)
    name = selected["name"]
    type_hint = selected["type"]
    
    # Generate hints
    first_letter = name[0]
    length = len(name)

    print("\n🧩 Guess the Pokémon!")
    print(f"Hint 1: It has {length} letters.")
    print(f"Hint 2: It starts with '{first_letter}'.")
    print(f"Hint 3: Its type is {type_hint}.")

    attempts = 0
    while True:
        guess = input("\nYour guess: ").strip().capitalize()
        attempts += 1
        if guess == name:
            print(f"✅ Correct! It was {name}. You guessed it in {attempts} attempts.")
            break
        else:
            print("❌ Nope! Try again.")

# Start the game
play_game()
