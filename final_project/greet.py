# ============================================================
# STUDENT IMPLEMENTATION FILE
# Complete each function below according to its docstring.
# Do not change the provided function names or parameters.
# ============================================================

import sys
import random

from game_utils import Player

from text import (
    REETING_MESSAGE,
    GREETING_REPEAT,
    WIZARD_STATS_MESSAGE,
    WIZARD_CHOICE_MESSAGE,
    VALID_WIZARD_CHOICES,
    WIZARD_REPEAT_MESSAGE,
    WIZARD_REROLL_MESSAGE,
    WIZARD_GAME_OVER_MESSAGE,
)

from constants import (
    STARTING_MONEY_LOW,
    STARTING_MONEY_HIGH,
    STARTING_HEALTH_LOW,
    STARTING_HEALTH_HIGH,
    STARTING_MIN_DMG_LOW,
    STARTING_MIN_DMG_HIGH,
    STARTING_MAX_DMG_LOW,
    STARTING_MAX_DMG_HIGH,
)


def check_name_validity(player_name: str) -> bool:
    """
    Check whether the player's name is valid.

    A valid player name must contain only letters.

    Args:
        player_name: The name entered by the player.

    Returns:
        True if the name contains only letters.
        False otherwise.
    """

    # HINT:
    # Remember the string method:
    # my_string.isalpha()

    pass


def randomize_stats() -> dict[str, int]:
    """
    Generate random starting statistics for the player.

    The player's starting money, health, minimum damage,
    and maximum damage should each be generated using the
    corresponding constants imported from constants.py.

    Returns:
        A dictionary containing the following keys:
        - "money"
        - "health"
        - "min_damage"
        - "max_damage"

        Each key should store its randomly generated integer value.
    """

    # HINT:
    # Use random.randint(low, high)
    # and the constants imported above.

    starting_money = ...
    starting_health = ...
    starting_min_dmg = ...
    starting_max_dmg = ...

    # Return a dictionary containing the four values above.
    return {
        "money": ...,
        "health": ...,
        "min_damage": ...,
        "max_damage": ...,
    }


def display_stats(stats: dict[str, int]):
    """
    Display the player's current randomly generated statistics.

    The function should display:
    - starting money
    - starting health
    - minimum damage
    - maximum damage

    Args:
        stats: A dictionary containing the player's generated
               starting statistics.
    """

    # HINT:
    # "Display" means print.
    #
    # Dictionary values can be accessed like:
    # stats["money"]

    print(WIZARD_STATS_MESSAGE)

    print(...)
    print(...)
    print(...)
    print(...)


def wizard_reroll(player_name: str) -> dict[str, int]:
    """
    Allow the player to accept or reroll their starting statistics.

    The player starts with one remaining letter per character
    in their name. Each reroll request consumes one letter.
    The player's actual name remains unchanged.

    Example: "Sam" allows two successful rerolls.
    Requesting a third reroll ends the game.

    The function should:
    1. Generate and display random starting statistics.
    2. Ask whether the player wants to keep or reroll them.
    3. Keep asking until a valid choice is entered.
       Invalid choices do not consume letters or regenerate stats.
    4. Return the current statistics if the player chooses "1".
    5. If the player chooses "2", subtract one remaining letter.
    6. If no letters remain, display the game-over message,
       pause for Enter, and end the program.
    7. Otherwise, generate new statistics and repeat.

    Args:
        player_name: The player's validated name.

    Returns:
        A dictionary containing the accepted starting statistics.
    """
    # The player begins with one letter for each character
    # in their name.
    letters_remaining = ...

    # Generate the first set of stats.
    stats = ...

    # Keep going until the player accepts their stats
    # or runs out of letters.
    while True:

        # Display the current stats.
        ...

        print(f"\nLetters remaining: {letters_remaining}")

        # Ask the player whether they want to keep or reroll.
        choice = ...

        # Validate the player's choice.
        while ...:
            choice = ...

        # Choice "1" means keep the current stats.
        if ...:
            return ...

        # Otherwise, the player chose to reroll.
        letters_remaining -= ...

        print(WIZARD_REROLL_MESSAGE)

        # If no letters remain, the game ends.
        if ...:
            print(WIZARD_GAME_OVER_MESSAGE)
            input("Press Enter to exit...")
            sys.exit()

        # Generate a new set of stats for the next loop.
        stats = ...


def initialize_player() -> Player:
    """
    Create and return the player's Player object.

    The function should:
    1. Ask the player to enter a name.
    2. Validate the name using check_name_validity().
    3. Continue asking until a valid name is entered.
    4. Allow the player to generate and reroll starting statistics
       using wizard_reroll().
    5. Create a Player object using the player's name and accepted
       starting statistics.
    6. Return the completed Player object.

    Returns:
        A Player object containing the player's name and
        starting statistics.
    """

    # Ask for the player's name.
    player_name = ...

    # Check whether the name is valid.
    is_name_valid = ...

    # Keep asking until a valid name is entered.
    while ...:
        player_name = ...
        is_name_valid = ...

    # Generate and accept the player's starting stats.
    stats = wizard_reroll(player_name)

    # Create the Player object.
    #
    # HINT:
    # Create the Player object using the accepted stats.
    # Use stats["health"] as the player's max_health.
    # Player automatically initializes current health to max_health.
    player = Player(
        name=...,
        money=...,
        max_health=...,
        min_damage=...,
        max_damage=...,
    )

    return ...