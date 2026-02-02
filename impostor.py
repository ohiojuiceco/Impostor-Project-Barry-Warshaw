import random
import os
import time

words = [
    "Pizza", "Sushi", "Elephant", "Giraffe", "Astronaut", "Submarine", "Keyboard", "Mountain", 
    "Bicycle", "Diamond", "Firefighter", "Library", "Dragon", "Volcano", "Rainbow", "Telescope", 
    "Cactus", "Skateboard", "Pancake", "Dolphin", "Castle", "Guitar", "Snowman", "Microscope", 
    "Pineapple", "Hammer", "Waterfall", "Butterfly", "Robot", "Spaceship", "Helicopter", "Campfire", 
    "Sandwich", "Octopus", "Pyramid", "Jungle", "Airplane", "Backpack", "Popcorn", "Penguin", 
    "Sofa", "Toaster", "Lighthouse", "Parachute", "Suitcase", "Violin", "Umbrella", "Kangaroo", 
    "Soccer", "Basketball", "Ice Cream", "Rollercoaster", "Mirror", "Flashlight", "Museum", "Cinema", 
    "Statue", "Bridge", "Compass", "Map", "Globe", "Anchor", "Camera", "Headphones", 
    "Smartphone", "Laptop", "Stadium", "Forest", "Desert", "Island", "Tornado", "Cloud", 
    "Starfish", "Shark", "Whale", "Squirrel", "Eagle", "Tiger", "Lion", "Monkey", 
    "Zebra", "Crocodile", "Donut", "Muffin", "Spaghetti", "Taco", "Sushi", "Burrito", 
    "Lemonade", "Chocolate", "Cookie", "Ballet", "Painting", "Sculpture", "Theater", "Concert", 
    "Festival", "Gardening", "Fishing", "Hiking", "Camping", "Surfing", "Skiing", "Bowling"
]

keep_playing = "y"

while keep_playing == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    num_input = input("Enter the number of players: ")
    num = int(num_input)
    
    names = []
    for i in range(num):
        player_name = input("Enter the name of player #" + str(i + 1) + ": ")
        names.append(player_name)
    
    secret_word = random.choice(words)
    impostor_index = random.randint(0, num - 1)
    impostor_name = names[impostor_index]
    
    for i in range(num):
        os.system('cls' if os.name == 'nt' else 'clear')
        input(names[i] + ", press Enter when you are ready to see your word...")
        
        if i == impostor_index:
            print("YOU ARE THE IMPOSTOR")
            print("You do not have a word. Try to blend in!")
        else:
            print("YOUR WORD IS: " + secret_word)
        
        input("\nPress Enter to clear the screen for the next person...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    print("All players have seen their roles. Start discussing!")
    input("ENTER WHEN YOU WANT TO REVEAL THE IMPOSTOR AND THE WORD")
    
    print("\n------------------------------")
    print("THE IMPOSTOR WAS: " + impostor_name)
    print("THE WORD WAS: " + secret_word)
    print("------------------------------\n")
    
    keep_playing = input("Play again? (y/n): ")

print("Goodbye!")