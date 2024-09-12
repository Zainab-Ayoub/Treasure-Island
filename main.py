#print(r'''
#                 
#                    ____...------------...____
#              _.-"` /o/__ ____ __ __  __ \o\_`"-._
#             .'     / /                    \ \     '.
#             |=====/o/======================\o\=====|
#             |____/_/________..____..________\_\____|
#             /   _/ \_     <_o#\__/#o_>     _/ \_   \
#             \_________\####/_________/
#              |===\!/========================\!/===|
#              |   |=|          .---.         |=|   |
#              |===|o|=========/     \========|o|===|
#              |   | |         \() ()/        | |   |
#              |===|o|======{'-.) A (.-'}=====|o|===|
#              | __/ \__     '-.\uuu/.-'    __/ \__ |
#              |==== .'.'^'.'.====|
#              |  _\o/   __  {.' __  '.} _   _\o/  _|
#              `""""-""""""""""""""""""""""""""-""""`
#''')


print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
answer1 = input("In which direction do you want to move? (left / right) ")
answer1 = answer1.lower()  # Convert input to lowercase
if answer1 == "left":
    answer2 = input("Do you want to swim or wait? ")
    answer2 = answer2.lower()  # Convert input to lowercase
    if answer2 == "wait":
        answer3 = input("Which door you want to choose? (red, yellow, blue) ")
        answer3 = answer3.lower()  # Convert input to lowercase
        if answer3 == "yellow":
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
