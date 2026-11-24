# ============================================================
# STUDENT IMPLEMENTATION FILE
# Complete each function below according to its docstring.
# Do not change the provided function names or parameters.
# ============================================================

from game_utils import Player
from text import (
    STORE_MESSAGE,
    VALID_STORE_CHOICES,
    STORE_REPEAT_MESSAGE,
)
from constants import (
    ROCK_PRICE,
    ROCK_MIN_DAMAGE_BONUS,
    PAPER_PRICE,
    PAPER_MAX_HEALTH_BONUS,
    SCISSORS_PRICE,
    SCISSORS_MAX_DAMAGE_BONUS,
    CROWN_PRICE,
)


def shop(player: Player):
    """
    Allow the player to visit the store and purchase items.

    The function should:
    1. Display the store menu and ask what the player wants to buy.
    2. Continue asking until a valid choice is entered.
       Invalid choices must not change the player's gold,
       inventory, health, or damage.
    3. Process the selected purchase or leave action.
    4. Repeat the menu until the player leaves or purchases the crown.

    The store contains the following items:

    Choice "1": Weighted Rock
        - Costs ROCK_PRICE gold.
        - Can only be purchased once.
        - Set player.has_weighted_rock to True.
        - Increase minimum damage by ROCK_MIN_DAMAGE_BONUS.

    Choice "2": Paper Armor
        - Costs PAPER_PRICE gold.
        - Can only be purchased once.
        - Set player.has_paper_armor to True.
        - Increase maximum health by PAPER_MAX_HEALTH_BONUS.
        - Leave current health unchanged.

    Choice "3": Sharpened Scissors
        - Costs SCISSORS_PRICE gold.
        - Can only be purchased once.
        - Set player.has_sharpened_scissors to True.
        - Increase maximum damage by SCISSORS_MAX_DAMAGE_BONUS.

    Choice "4": Crown of the Three Hands
        - Costs CROWN_PRICE gold.
        - Can only be purchased once.
        - Set player.has_crown to True.
        - Immediately leave the store after a successful purchase.
          The main game handles displaying the win message.

    For each purchase attempt:
        - Check whether the player already owns the item first.
        - If already owned, display an appropriate message.
        - Otherwise, check whether the player has at least the price.
          A player with exactly the required gold can buy the item.
        - If affordable, subtract the price exactly once and apply
          the item's ownership flag and bonus, when applicable.
        - Display a message confirming a successful purchase.
        - If unaffordable, display an insufficient-gold message.
        - Rejected purchases must leave all player attributes unchanged.

    Choice "5": Leave
        - Display a departure message.
        - Leave all player attributes unchanged.
        - Exit the store and return to the main game.

    Pause for Enter after each purchase attempt while the player
    remains in the store, including unsuccessful attempts.
    Do not pause when leaving or successfully purchasing the crown.

    Args:
        player: The Player object representing the current player.
    """

    # Keep displaying the store until the player chooses to leave
    # or purchases the crown.
    still_shopping = True

    while still_shopping:

        # Ask the player what they would like to buy.
        player_store_choice = ...

        # Validate the player's choice.
        while ...:
            player_store_choice = ...

        # ----------------------------------------------------
        # CHOICE 1: WEIGHTED ROCK
        # ----------------------------------------------------
        if ...:

            # First, check whether the player already owns it.
            if ...:
                print("You already own a Weighted Rock!")

            # Otherwise, check whether the player can afford it.
            elif ...:

                # Subtract the price from the player's money.
                # HINT: Look at the Player methods in game_utils.py.
                ...

                # Mark the item as owned.
                player.has_weighted_rock = ...

                # Apply the minimum-damage bonus.
                # HINT: Look at the Player methods in game_utils.py.
                ...

                print("You bought a Weighted Rock!")
                print(
                    f"Your minimum damage has increased to "
                    f"{player.min_damage}."
                )

            else:
                print("You do not have enough gold.")

        # ----------------------------------------------------
        # CHOICE 2: PAPER ARMOR
        # ----------------------------------------------------
        elif ...:

            if ...:
                print("You already own Paper Armor!")

            elif ...:

                # Pay for the item.
                ...

                # Mark the item as owned.
                player.has_paper_armor = ...

                # Apply the maximum-health bonus.
                ...

                print("You bought Paper Armor!")
                print(
                    f"Your max health has increased to "
                    f"{player.max_health}."
                )

            else:
                print("You do not have enough gold.")

        # ----------------------------------------------------
        # CHOICE 3: SHARPENED SCISSORS
        # ----------------------------------------------------
        elif ...:

            if ...:
                print("You already own Sharpened Scissors!")

            elif ...:

                # Pay for the item.
                ...

                # Mark the item as owned.
                player.has_sharpened_scissors = ...

                # Apply the maximum-damage bonus.
                ...

                print("You bought Sharpened Scissors!")
                print(
                    f"Your maximum damage has increased to "
                    f"{player.max_damage}."
                )

            else:
                print("You do not have enough gold.")

        # ----------------------------------------------------
        # CHOICE 4: CROWN OF THE THREE HANDS
        # ----------------------------------------------------
        elif ...:

            # Check whether the player already owns the crown.
            if ...:
                print("You already have the Crown of the Three Hands!")

            # Otherwise, check whether the player can afford it.
            elif ...:

                # Pay for the crown.
                ...

                # The crown is the game's win condition.
                player.has_crown = ...

                print("You bought the Crown of the Three Hands!")
                print(
                    "You now possess the legendary prize of "
                    "Rock, Paper, Scissors!"
                )

                # Leave the store immediately after purchasing it.
                # We do this because it is the win condition of our game.
                still_shopping = ...

            else:
                print("You do not have enough gold.")

        # ----------------------------------------------------
        # CHOICE 5: LEAVE
        # ----------------------------------------------------
        elif ...:
            print("You leave the shop.")
            still_shopping = ...

        # Pause only if the player is staying in the store.
        if still_shopping:
            input("Press Enter to continue...")