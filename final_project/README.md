# IS 2053 Final Project

## Rock, Paper, Scissors Adventure

For your final project, you will work in groups to complete a partially built Python game.

Your player uses the town as a hub to, fight enemies, earn gold, purchase upgrades, rest at the inn. To win the game, the player must save up enough money and purchase the **Crown of the Three Hands**.

You are **not** starting from an empty project. Several files are already complete. Your job is to read the provided code and complete the unfinished functions.

---

# Project Goal

Your completed game should allow the player to:

1. Create a character.
2. Receive and reroll randomized starting statistics.
3. View current statistics and inventory.
4. Visit the store.
5. Purchase upgrades.
6. Visit the inn and restore health.
7. Fight enemies using Rock, Paper, Scissors.
8. Earn gold from battles.
9. Purchase the **Crown of the Three Hands** and win the game.

Run the game with:

```bash
python game.py
```

---

# Project Files

```text
final_project/
│
├── game.py
├── game_utils.py
├── constants.py
├── text.py
│
├── greet.py
├── town.py
├── store.py
├── inn.py
└── battle_ground.py
```

## Provided Files — Do Not Modify

The following files are already complete:

```text
game.py
game_utils.py
constants.py
text.py
```

### `game.py`

Contains `main()` and controls the overall flow of the game.

### `game_utils.py`

Contains the `Player` and `Enemy` classes.

Read this file carefully. It contains attributes and methods your code will need, such as:

```python
player.money
player.health
player.take_damage(...)
player.refill_health()
player.pay_gold(...)
```

### `constants.py`

Contains shared values such as prices, starting-stat ranges, and item bonuses.

### `text.py`

Contains menus, messages, and valid menu choices.

---

# Files Your Team Must Complete

Your team must complete:

```text
greet.py
town.py
store.py
inn.py
battle_ground.py
```

Each unfinished function already includes:

* its function name
* parameters
* type hints
* a docstring explaining what it must do
* a `pass` statement

Replace `pass` with working Python code.

Do **not** rename functions or change their provided parameters or return types. Other parts of the program depend on these function definitions.

---

# How the Game Fits Together

```text
START
  |
  v
Create Player
greet.py
  |
  v
TOWN
town.py
  |
  +----> STORE ----+
  |      store.py  |
  |                |
  +----> BATTLE ---+
  | battle_ground.py
  |                |
  +----> INN ------+
  |      inn.py    |
  |                |
  +----> EXIT      |
  |                |
  +<---------------+
  |
  v
Purchase Crown
  |
  v
YOU WIN
```

The same `Player` object moves through the different parts of the game.

Changes to:

```python
player.money
player.health
player.min_damage
player.max_damage
player.has_crown
```

remain with the player throughout the game.

---

# Working as a Team

This is a team project using one shared GitHub repository.

Divide the unfinished modules among your group so multiple people can work at the same time.

Every team member must:

* contribute meaningful Python code
* make meaningful Git commits
* help test and debug the final program

Do not wait until the end to make one large commit.

Good commit messages describe the work completed, for example:

```text
Implement store purchasing logic

Add inn input validation

Complete RPS winner function

Fix battle rewards
```

---

# Before You Begin

Before writing code:

1. Run the starter project.
2. Read `game.py`.
3. Read `game_utils.py`.
4. Look through `constants.py` and `text.py`.
5. Read all unfinished function docstrings.
6. Decide how your team will divide the work.

---

# Testing

Test your code as you work.

Your final program should correctly handle situations such as:

* invalid names
* invalid menu choices
* rerolling starting stats
* buying items
* not having enough gold
* buying the same item twice
* resting at the inn
* winning, losing, and drawing RPS rounds
* defeating an enemy
* losing a battle
* running from battle
* earning gold
* purchasing the Crown of the Three Hands

Do not test only one path through the game.

---

# Use What You Learned

This project combines concepts from throughout the semester, including:

* input and output
* variables and data types
* conditionals
* loops
* input validation
* functions and return values
* type hints
* dictionaries
* random numbers
* imports and custom modules
* classes and objects

Work **one function at a time**. Read its docstring, determine what it needs to do, implement it, test it, and commit your work.

The goal is to combine the programming concepts you have learned into one larger collaborative program.

**Obtain the Crown of the Three Hands.**