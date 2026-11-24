# ============================================================
# STUDENT IMPLEMENTATION FILE
# Complete each function below according to its docstring.
# Do not change the provided function names or parameters.
# ============================================================

from game_utils import Player
from text import (
    INN_MESSAGE,
    VALID_INN_CHOICES,
    INN_REPEAT_MESSAGE,
)
from constants import INN_PRICE


def rest(player: Player):
    """
    Allow the player to visit the inn and restore their health.

    The function should:
    1. Display the inn menu and ask whether the player wants
       to rest ("1") or leave ("2").
    2. Continue asking until a valid choice is entered.
       Invalid choices must not change the player's gold or health.
    3. If the player chooses to rest and has at least INN_PRICE gold:
       - Subtract INN_PRICE from their gold.
       - Restore their current health to their maximum health.
       - Display a message confirming that they rested.
       - Keep the player in the inn.
    4. If the player chooses to rest without enough gold:
       - Display a message explaining that they cannot afford the inn.
       - Leave their gold and health unchanged.
       - Send the player out of the inn.
    5. If the player chooses to leave:
       - Display a departure message.
       - Leave their gold and health unchanged.
       - Exit the inn.
    6. Pause for Enter after each valid action, including leaving
       or being unable to afford rest.
    7. Repeat the menu while the player remains in the inn.

    Resting costs INN_PRICE gold even when health is already full.
    A player with exactly INN_PRICE gold can rest.

    Args:
        player: The Player object representing the current player.
    """
    # Keep the player in the inn until they choose to leave
    # or cannot afford to stay.
    is_player_inning = True

    while is_player_inning:

        # Ask the player whether they want to rest or leave.
        player_inn_choice = ...

        # Validate the player's choice.
        while ...:
            player_inn_choice = ...

        # Choice "1" means the player wants to rest.
        if ...:

            # Check whether the player has enough gold.
            # HINT: look at the player class' attributes.
            if ...:

                # Pay for the room.
                # HINT: Look at the methods available in the Player class.
                ...

                # Restore the player's health to full.
                # HINT: Look at the methods available in the Player class.
                ...

                print("You stay the night at the inn.")
                print("Your health is back to full!")

            else:
                print("You don't have enough gold to rest here!")
                print("You leave the inn.")

                # End the inn loop.
                is_player_inning = ...

        # Choice "2" means the player wants to leave.
        elif ...:
            print("You leave the inn.")

            # End the inn loop.
            is_player_inning = ...

        input("Press Enter to continue...")