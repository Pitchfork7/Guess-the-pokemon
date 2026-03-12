import requests

def Pokedex():
    play = False
    num = 151

    option = input("Input NAME or ID (N/ID)").upper()
    if option == "N":
        num = input("enter pokemon name> ")
        play = True
    elif option == "ID":
        num = int(input("enter pokemon num> "))
        play = True
    else:
        print("not an option")
        play = False

    # The URL for Pokémon #14 (Kakuna)
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"

    # Fetch the data directly from PokeAPI
    response = requests.get(url)

    # Convert the response into a Python dictionary
    poke = response.json()

    if play:
        types = [t['type']['name'].capitalize() for t in poke['types']]
        print(f"Name: {poke['name'].capitalize()}")
        print(f"Type(s): {', '.join(types)}")
        print(f"Base Experience: {poke['base_experience']}")
        print(f"Height: {poke['height']}")
        print(f"Weight: {poke['weight']}")



print("1. Guess that Pokemon!")
print("2. Pokedex")

menuop = str(input("Enter > "))

if menuop == "1":
    print("Game coming soon...")
elif menuop == "2":
    Pokedex()
else:
    print("Not valid")




