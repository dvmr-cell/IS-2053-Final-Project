# python ./final_project/game.py
# ============================================================
# PROVIDED FILE - DO NOT MODIFY
# ============================================================
#
# This file controls the overall flow of the game.
# Complete the functions in the other project files so that
# this program runs correctly.
#
# Run the completed game with:
# python game.py
# ============================================================
import sys
from game_utils import Player
from greet import initialize_player
from town import chose_what_to_do
from store import shop
from inn import rest
from battle_ground import battle


def you_win(player: Player):
    print(f"\nCongratulations, {player.name}!")
    print("You obtained the Crown of the Three Hands!")
    print("You win the game!")
    input("Press Enter to exit...")
    exit()


def main():
    player = initialize_player()

    while not player.has_crown:
        # ask player if they want to battle, shop, or quit
        game_state = chose_what_to_do(player)

        # if they choose battle, they play rock paper scissors.
        if game_state == "1": 
            shop(player)
        elif game_state == "2": 
            battle(player)
        elif game_state == "3": 
            rest(player)
        elif game_state == "exit": 
            print("Thanks for playing. Sorry to see you leave!")
            input("Press Enter to exit...")
            sys.exit()

    you_win(player)


if __name__ == "__main__":
    main()