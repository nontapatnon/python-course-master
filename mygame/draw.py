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
