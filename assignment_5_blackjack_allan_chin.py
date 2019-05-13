"""
Assignment 5

This program plays a game of blackjack with the user

"""

import random
import time
from colorama import Fore, Style, init
init()

CARD_DIC = {1: 'Ace', 2:  '2', 3: '3', 4: '4', 5: '5',
            6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
            11: 'Jack', 12: 'Queen', 13: 'King'}

def gen_num():
    """
    generates a random number from 1-13
    """
    return random.randint(1, 13)

def want_to_play():
    """
    Asks the user if he wants to play again
    """
    print(f'{"":-^66}')
    while True:
        try:
            answer = input("\n\nDo you want to start a new game? (y/n): ")
            if answer.lower() == 'y':
                play_game()
            elif answer.lower() == 'n':
                print("\n\nHave a nice day!")
                break
            else:
                print("\n\nThat is not y or n.")
        except ValueError:
            print("\n\nThat is not a valid answer. ")


def cal_value(value):
    """
    Calculates the card value
    Ace is 11, but turns to 1 if value is higher than 21
    Jack, Queen, King turns to value 10
    """
    total = 0
    for index in value:
        if index == 1:
            total = total + 11
            if total > 21:
                total = total - 10
        elif index >= 11:
            total = total + 10
        else:
            total = total + index
    return total

def colour(number, var):
    """
    add colour to cards
    if its var 1 change the card to blue colour
    if not change int to string and make total yellow
    """
    if var == 1:
        return Fore.GREEN + CARD_DIC[number] + Style.RESET_ALL
    number = str(number)
    return Fore.CYAN + number + Style.RESET_ALL

def dealer_turn(player_cards, dealer_cards):
    """
    Dealers turn to play
    Show hidden card
    Dealer must hit if he is lower than player and lower than 17
    Dealer wins if he did not bust and is higher or equal player
    """
    #reveal dealer cards
    print(f"\n\nDealers turn to play!")
    print(f"\n\nThe dealer draws a {colour(dealer_cards[0], 1)} " +
          f"and a {colour(dealer_cards[1], 1)}. "  +
          f"Dealer's total is {colour(cal_value(dealer_cards), 2)}.")
    time.sleep(2)

    #add cards to dealer
    while   (cal_value(dealer_cards) < cal_value(player_cards) and
             cal_value(dealer_cards) <= 16):
        dealer_cards.append(gen_num())
        print(f"\n\nDealer draws a {colour(dealer_cards[-1], 1)}. " +
              f"Dealer's total is {colour(cal_value(dealer_cards), 2)}.")
        time.sleep(2)

    #final result if dealer wins/loses
    if      (cal_value(dealer_cards) >= cal_value(player_cards) and
             cal_value(dealer_cards) < 22):
        print(f"\n\nDealer wins.")
    else:
        print(f"\n\nDealer loses.")

def player_turn(cards):
    """
    Players turn to play
    Ask the user if he wants to get another card or stay
    if user gets higher than 21 or stands, break out
    """
    #show initial player cards
    print(f"\n\nYour cards are {colour(cards[0], 1)} and " +
          f"a {colour(cards[1], 1)}. "  +
          f"Your total is {colour(cal_value(cards), 2)}.")

    #player drawing cards
    while cal_value(cards) < 21:
        answer = input("\n\nHit or stand? (h/s): ")
        if answer.lower() == 'h':
            cards.append(gen_num())
            print(f"\n\nHit! You drew a {colour(cards[-1], 1)}. " +
                  f"Your total is {colour(cal_value(cards), 2)}.")
        elif answer.lower() == 's':
            break
        else:
            print(f"\n\nThat wasn't a valid answer. Try again.")
            print(f"\n\nYour total is {colour(cal_value(cards), 2)}.")

def play_game():
    """
    plays the game
    shows dealers cards
    goes to players turn function
    if player cards value is greater than 21, he bust
    if he is not go to dealer turn
    """
    #generate number
    player_cards = [gen_num(), gen_num()]
    dealer_cards = [gen_num(), gen_num()]

    #show initial dealer dealer cards
    print(f"\n\nThe dealer draws a {colour(dealer_cards[0], 1)} " +
          f"and a hidden card. ")

    #players turn
    player_turn(player_cards)

    #if player still has less than 22 go to dealer
    #if not, bust
    if cal_value(player_cards) <= 21:
        dealer_turn(player_cards, dealer_cards)
    else:
        print(f"\n\nBusted! You lose.")

def main():
    """
    This is the main program
    """
    print(Fore.YELLOW + "\nLet's play Blackjack" + Style.RESET_ALL)
    want_to_play()

if __name__ == '__main__':
    main()
