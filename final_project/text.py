from constants import (
    INN_PRICE,
    ROCK_PRICE,
    PAPER_PRICE,
    SCISSORS_PRICE,
    CROWN_PRICE,
)

###############################################
# GREETING
###############################################

GREETING_MESSAGE = """\
Hello, Traveler! Welcome to the world of Ur.
This is a land of shopping and fighting.
What shall we call you in this strange land?

"""

GREETING_REPEAT = """\
Sorry, names here must be nonempty and contain only letters.
Spaces, numbers, and punctuation are not allowed.

"""

###############################################
# WIZARD
###############################################

WIZARD_STATS_MESSAGE = """\
The wizard waves his hands and reveals your starting stats:
"""

WIZARD_CHOICE_MESSAGE = """\
You may accept these stats, or ask the wizard to reroll them.

But beware...
Each reroll will cost you one remaining letter.
If you run out of letters, you will cease to exist!
Your character's actual name remains unchanged.

Enter "1" to keep these stats
Enter "2" to reroll

"""

VALID_WIZARD_CHOICES = [
    "1",
    "2",
]

WIZARD_REPEAT_MESSAGE = """\
Sorry, please enter a valid option.

Enter "1" to keep these stats
Enter "2" to reroll

"""

WIZARD_REROLL_MESSAGE = """\
The wizard takes one of your remaining letters...
"""

WIZARD_GAME_OVER_MESSAGE = """\
The wizard takes your final letter.

You have no letters left.
Without a name, you cease to exist.

GAME OVER
"""

###############################################
# TOWN
###############################################

MAIN_SCREEN = """\
~PLAYERNAME~, what would you like to do?
Enter "1" for shopping
Enter "2" for fighting
Enter "3" for sleep
Or type "exit" if you are done with this nonsense!

"""

VALID_MAIN_CHOICES = [
    "1",
    "2",
    "3",
    "exit",
]

MAIN_REPEAT_MESSAGE = """\
Sorry, please enter a valid option.
Enter "1" for shopping
Enter "2" for fighting
Enter "3" for sleep
Or type "exit" if you are done with this nonsense!

"""

###############################################
# FIGHT OR RUN
###############################################

FIGHT_RUN_MESSAGE = """\
You find yourself in an intense battle with ~ENEMYNAME~!
You have ~HEALTH~ points of health.
What will you do?!
Enter "1" to fight
Enter "2" to run

"""

VALID_FIGHT_RUN_CHOICES = [
    "1",
    "2",
]

FIGHT_RUN_REPEAT_MESSAGE = """\
Sorry, please enter either "1" or "2".

"""

###############################################
# ROCK, PAPER, SCISSORS
###############################################

RPS_MESSAGE = """\
You stand your ground and fight!
Enter "1" for Rock
Enter "2" for Paper
Enter "3" for Scissors

"""

VALID_RPS_CHOICES = [
    "1",
    "2",
    "3",
]

RPS_REPEAT_MESSAGE = """\
Sorry, please enter either "1", "2", or "3".

"""

###############################################
# INN
###############################################

INN_MESSAGE = f"""\
You enter a small inn.
A room for the night costs {INN_PRICE} gold.
Would you like to rest?
Enter "1" to stay the night
Enter "2" to leave the inn

"""

VALID_INN_CHOICES = [
    "1",
    "2",
]

INN_REPEAT_MESSAGE = """\
Sorry, please enter either "1" or "2".
Enter "1" to stay the night
Enter "2" to leave the inn

"""

###############################################
# STORE
###############################################

STORE_MESSAGE = f"""\
Welcome to the Rock, Paper, Scissors Emporium!

What would you like to buy?

Enter "1" for Weighted Rock             - {ROCK_PRICE} gold
Enter "2" for Paper Armor               - {PAPER_PRICE} gold
Enter "3" for Sharpened Scissors        - {SCISSORS_PRICE} gold
Enter "4" for Crown of the Three Hands  - {CROWN_PRICE} gold

Enter "5" to leave the shop

"""

VALID_STORE_CHOICES = [
    "1",
    "2",
    "3",
    "4",
    "5",
]

STORE_REPEAT_MESSAGE = """\
Sorry, please enter a valid option.

Enter "1" for Weighted Rock
Enter "2" for Paper Armor
Enter "3" for Sharpened Scissors
Enter "4" for Crown of the Three Hands
Enter "5" to leave the shop

"""