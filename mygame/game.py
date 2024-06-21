# game.py

# option1
# import the draw module
from draw import draw_game, clear_screen, main_screen

def play_game():
    result = "Player won!"
    return result
    
def main():
    print("Game started")
    main_screen
    result = play_game()
    draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

'''
# option2 Importing module objects to the current namespace
# import the draw module

from draw import draw_game, clear_screen, main_screen

def play_game():
    result = "Player won!"
    return result

def main():
    print("Game started")
    main_screen
    result = play_game()
    draw_game(result)

# ----------------------------------
# option3 Importing all objects from a module
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

# ----------------------------------

'''