# ============================================================
# STUDENT IMPLEMENTATION FILE
# Complete each function below according to its docstring.
# Do not change the provided function names or parameters.
# ============================================================
import sys
import random

from game_utils import Player, Enemy
from text import (
    FIGHT_RUN_MESSAGE,
    VALID_FIGHT_RUN_CHOICES,
    FIGHT_RUN_REPEAT_MESSAGE,
    RPS_MESSAGE,
    VALID_RPS_CHOICES,
    RPS_REPEAT_MESSAGE,
)
from constants import RPS_MAP


#######################################################
# HELPERS
#######################################################

def check_if_win_or_dead(
    player: Player,
    enemy: Enemy
) -> tuple[bool, str]:
    """
    Check whether the battle has ended.

    The battle is over when either:
    - the enemy's health is 0 or less
    - the player's health is 0 or less

    Returns:
        A tuple containing:
        - a Boolean indicating whether the fight is over
        - a string identifying the winner

        The winner should be:
        - "player" if the enemy has been defeated
        - "enemy" if the player has been defeated
        - an empty string if the battle is still continuing
    """

    # Start by assuming the fight is still going.
    fights_over = False
    winner = ""

    # If the enemy has no health left,
    # the player won.
    # HINT: look at what attributes the enemy has
    if ...:
        fights_over = ...
        winner = ...

    # Otherwise, if the player has no health left,
    # the enemy won.
    # HINT: look at what attributes the player has
    elif ...:
        fights_over = ...
        winner = ...

    # Return BOTH values as a tuple.
    return ..., ...


def fight_or_run(player: Player, enemy: Enemy) -> str:
    """
    Ask the player whether they want to fight or run.

    The function should:
    1. Display the fight-or-run message.
    2. Include the enemy's name in the message.
    3. Include the player's current health in the message.
    4. Ask the player to choose whether to fight or run.
    5. Validate the player's choice.
    6. Continue asking until a valid choice is entered.
    7. Return the valid choice.

    Args:
        player: The Player object representing the current player.
        enemy: The Enemy object representing the current enemy.

    Returns:
        The player's validated fight-or-run choice as a string.
    """

    # Start with the provided fight message.
    fight_message = FIGHT_RUN_MESSAGE

    # Replace the placeholders in the message.
    #
    # HINT: look at the fight_run_message
    # Replace ~ENEMYNAME~ with the enemy's name.
    # Replace ~HEALTH~ with the player's current health as a string.
    # my_string.replace("old text", "new text")
    fight_message = ...
    fight_message = ...

    # Ask the player whether they want to fight or run.
    fight_run_choice = ...

    # Validate the player's choice.
    while ...:
        fight_run_choice = ...

    return ...


def determine_rps_winner(
    player_rps_choice: int,
    enemy_rps_choice: int
) -> int:
    """
    Determine the winner of one Rock-Paper-Scissors round.

    The choices use the following values:
    - 1 = Rock
    - 2 = Paper
    - 3 = Scissors

    The function should:
    1. Display the player's choice.
    2. Display the enemy's choice.
    3. Determine whether the player wins, loses, or draws.
    4. Display an appropriate message describing the result.

    Returns:
        1 if the player wins.
        2 if the enemy wins.
        3 if the round is a draw.
        note we are returning integers not strings.
    """

    # RPS_MAP converts the numbers 1, 2, and 3
    # into the words Rock, Paper, and Scissors.
    player_choice_text = RPS_MAP[...]
    enemy_choice_text = RPS_MAP[...]

    print()
    print(f"You picked: {player_choice_text}")
    print(f"They picked: {enemy_choice_text}")
    print()

    # If both choices are the same, it is a draw.
    if ...:
        print(f"You both chose {player_choice_text}")
        return ...

    # Otherwise, check all three ways the player can win.
    elif (
        # Rock beats Scissors
        (...)
        or
        # Paper beats Rock
        (...)
        or
        # Scissors beat Paper
        (...)
    ):
        print(
            f"You win! {player_choice_text} "
            f"beats {enemy_choice_text}"
        )
        return ...

    # If it was not a draw and the player did not win,
    # the enemy must have won.
    else:
        print(
            f"You lose! {enemy_choice_text} "
            f"beats {player_choice_text}"
        )
        return ...


def handle_outcome(
    rps_outcome: int,
    player: Player,
    enemy: Enemy
):
    """
    Apply damage based on the result of a Rock-Paper-Scissors round.

    If the player wins:
    - Generate a random amount of damage between the player's
      minimum and maximum damage.
    - Apply that damage to the enemy.
    - Display the amount of damage dealt.

    If the enemy wins:
    - Generate a random amount of damage between the enemy's
      minimum and maximum damage.
    - Apply that damage to the player.
    - Display the amount of damage taken.

    If the round is a draw:
    - No damage should be dealt.

    Args:
        rps_outcome: The result of the Rock-Paper-Scissors round.
        player: The Player object representing the current player.
        enemy: The Enemy object representing the current enemy.
    """

    # Outcome 1 means the player won the RPS round.
    # HINT: rps_outcome is an integer: 1 = player wins, 2 = enemy wins, 3 = draw.
    if ...:

        # Generate damage using the player's damage range.
        dmg_amount = random.randint(
            ...,
            ...
        )

        print(f"You deal {dmg_amount} damage to the enemy!")

        # Apply damage to the enemy.
        # HINT: Look at the Enemy methods in game_utils.py.
        ...

    # Outcome 2 means the enemy won the RPS round.
    elif ...:

        # Generate damage using the enemy's damage range.
        dmg_amount = random.randint(
            ...,
            ...
        )

        print(f"You take {dmg_amount} damage!")

        # Apply damage to the player.
        ...

    # Outcome 3 is a draw, so no damage occurs.
    elif ...:
        pass


def rps(player: Player, enemy: Enemy) -> int:
    """
    Run one Rock-Paper-Scissors round.

    The function should:
    1. Ask the player to choose Rock, Paper, or Scissors.
    2. Validate the player's choice.
    3. Convert the player's valid choice to an integer.
    4. Generate the enemy's choice.
    5. Determine the winner using determine_rps_winner().
    6. Return the result of the round.

    Args:
        player: The Player object representing the current player.
        enemy: The Enemy object representing the current enemy.

    Returns:
        1 if the player wins.
        2 if the enemy wins.
        3 if the round is a draw.
    """

    # Ask the player to choose Rock, Paper, or Scissors.
    player_rps_choice = ...

    # Validate the player's choice.
    while ...:
        player_rps_choice = ...

    # The player's input is currently a string.
    # Convert it to an integer.
    player_rps_choice = ...

    # Ask the Enemy object to generate its RPS choice.
    # HINT: Look at the Enemy methods in game_utils.py.
    enemy_rps_choice = ...

    # Determine who won the round.
    rps_outcome = ...

    return ...


def flee():
    """
    Display a message indicating that the player fled the battle
    and returned to town.
    """

    print(...)


def defeat():
    """
    Handle the player losing the battle.

    The function should:
    1. Tell the player that their health reached zero.
    2. Display a game-over message.
    3. Pause until the player presses Enter.
    4. End the program.
    """

    print(...)
    print(...)

    # Pause before ending the program.
    # Hint: use an input() without assignment
    ...

    # End the program.
    sys.exit()


def victory(player: Player, enemy: Enemy):
    """
    Handle the player winning the battle.

    The function should:
    1. Display a message identifying the defeated enemy.
    2. Generate a random gold reward from 5 through 10.
    3. Display the amount of gold earned.
    4. Add the gold reward to the player's money.

    Args:
        player: The Player object representing the current player.
        enemy: The defeated Enemy object.
    """

    print()

    # Display the defeated enemy's name.
    print(...)

    # Generate a random reward from 5 through 10 gold.
    gold = ...

    print(...)

    # Add the reward to the player's money.
    player.money += ...


#######################################################
# MAIN FUNCTION
#######################################################

def battle(player: Player):
    """
    Run one complete battle encounter.

    The function should:
    1. Create an Enemy named "Clarg'ar" with:
       - 6 health
       - minimum damage of 1
       - maximum damage of 3
    2. Ask the player once whether they want to fight or run.
    3. If the player runs:
       - call flee()
       - end the battle
    4. If the player fights:
       - repeatedly play Rock-Paper-Scissors rounds
       - apply the result of each round
       - check whether the player or enemy has been defeated
    5. If the player chooses to fight, continue until either the player or enemy has health of 0 or less.
    6. If the player is defeated, call defeat().
    7. If the enemy is defeated, call victory().
    8. Pause before returning to the town.

    Args:
        player: The Player object representing the current player.
    """

    # Create the enemy for this battle.
    enemy = Enemy(
        name=...,
        health=...,
        min_damage=...,
        max_damage=...
    )

    # Ask the player whether they want to fight or run.
    fight_run_choice = ...

    # Start by assuming that the fight is still going
    # and that there is no winner yet.
    fights_over = False
    winner = ""

    # Continue until the battle ends.
    while not fights_over:

        # Choice "1" means fight.
        if ...:

            # Play one RPS round.
            rps_outcome = ...

            # Apply damage based on the outcome.
            ...

        # Choice "2" means run.
        elif ...:

            # Display the flee message.
            ...

            # End the battle loop.
            fights_over = ...
            break

        # Check whether either character has reached zero health.
        fights_over, winner = ...

        # Pause between rounds if the battle is still going.
        if not fights_over:
            input("Press Enter to continue...")

    # Handle the final result.
    if winner == ...:
        ...

    elif winner == ...:
        ...

    # Pause before returning to town.
    input("Press Enter to continue...")