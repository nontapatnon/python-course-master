---
layout: page
title: Resources
---


<!-- * For Python script in class [Download](https://nontapatnon.github.io/python-course-master/Teaching/python.py) -->

<!-- * For Python script in class [This](https://nontapatnon.github.io/python-course-master/Teaching/python.py 'Link title')

* For Python script in class [This](https://nontapatnon.github.io/python-course-master/Teaching/python.txt 'Link title') -->


## For the Python script in this class (July 2024) is below:

```
# First Python Programming

# print("Hello, World!")

# Variables and Data Types

# Numbes
# Integer or int
# number =  7

# print(number)

# print(type(number))

# Float
# number = 8.135464654
# print(number)
# print(round(number, 2))
# print(type(number))

# String or str
text = "123"

print(type(text))
print(text)
print(123)

```

## Modules and Packages

**game.py**
```
# game.py

# option1
# import the draw module
import draw

def play_game():
    result = "Player won!"
    return result

def main():
    print("Game started")
    # Use the main_screen object from the draw module
    draw.main_screen
    result = play_game()
    draw.draw_game(result)
    draw.clear_screen()

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
    clear_screen()

# ----------------------------------
# option3 Importing all objects from a module
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

# ----------------------------------

'''

'''
# option2 Importing module objects to the current namespace
# import the draw module

from draw import draw_game

def main():
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
```

**draw.py**
```
# draw.py

def draw_game(result):
    print(f"Game result: {result}")

def clear_screen():
    print("Screen cleared")

class Screen:
    def __init__(self):
        print("Screen initialized")

# initialize main_screen as a singleton
main_screen = Screen()
```
