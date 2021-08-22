import random


def get_hand():
    hand_input = input("Enter your hand: ")
    return hand_input


def get_random_hand(hands_list: list) -> str:
    random_selection = random.choice(hands_list)
    return random_selection


def is_winnable(user_hand: str, machine_hand: str) -> bool:
    if (user_hand == "rock" and machine_hand == "scissors") or (user_hand == "paper" and machine_hand == "rock") or (user_hand == "scissors" and machine_hand == "paper"):
        return True
    else:
        return False


def is_in_hands(user_hand: str, hands_list: list) -> bool:
    if user_hand in hands_list:
        return True
    else:
        return False


def main():
    hands = ["rock", "paper", "scissors"]
    while True:
        random_hand = get_random_hand(hands)
        user_try = get_hand()
        if is_winnable(user_try.lower(), random_hand):
            print("You win!\n")
            break
        elif user_try.lower() == random_hand:
            print("It's a tie!\n")
        else:
            if is_in_hands(user_try, hands):
                print("You lose!\n")
            else:
                print("Invalid input. Try again.\n")


main()
