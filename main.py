import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_action():
    choices = [f"{action.name}[{action.value}]" for action in Action ]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_action():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors. You Win!")
        else:
            print("Paper covers rock. You Lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock. You Win!")
        else:
            print("Scissors cut paper. You Lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper. You Win!")
        else:
            print("Rock smashes scissors. You Lose")

while True:
    try:
        user_action = get_user_action()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_action()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n)")
    if play_again.lower() != "y":
        break
