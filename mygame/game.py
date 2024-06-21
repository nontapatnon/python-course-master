# game.py
import draw

def play_game():
    result = "Player won!"
    return result

def main():
    result = play_game()
    draw.draw_game(result)

if __name__ == '__main__':
    main()
