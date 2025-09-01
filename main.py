print("Welcome to the Band Name Generator")
finish = False
while not finish:
    city_name = input("What's the name of the city you grew up in? ")
    pet_name = input("What's your pet's name? ")
    print(f"Your band name could be {city_name} {pet_name}")

    question = input("\nType 'n' to finsh!!! ").lower()
    if question == "n":
        finish = True
