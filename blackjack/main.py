############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

def draw_card(num_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_drawn = []
    for i in range (0, num_cards):
        cards_drawn.append(random.choice(cards))
    return cards_drawn

def game_status(player_hand, computer_hand):
    player_hand = hand_value(player_hand)
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")
    return sum(player_hand)

def score_game(player_hand, computer_hand):
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    if player_hand == [10,11] or player_hand == [11,10]:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif player_score < 21:
        if player_score == computer_score:
            return "Draw 🙃"
        elif computer_score >= 21:
            return "Opponent went over. You win 😁"
        elif player_score > computer_score:
            return "You win 😃"
        elif player_score < computer_score:
            return "You lose 😤"

def computer_plays(computer_hand):
    computer_score = sum(computer_hand)
    while computer_score < 17:
        computer_hand += draw_card(1)
        computer_score = sum(computer_hand)
    return computer_hand

def hand_value(hand):
    if sum(hand) > 21:
        for i, card in enumerate(hand):
            if card == 11:
                hand[i] = 1
                if sum(hand) <= 21:
                    break
    return hand


if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    keep_playing = True
else:
    quit()

def blackjack():
    player_hand = []
    computer_hand = []

    while keep_playing == True:
        print(logo)
        
        player_hand = draw_card(2)
        computer_hand = draw_card(2)
        player_score = game_status(player_hand, computer_hand)

        while player_score < 21:
            player_draws = input("Type 'y' to get another card, type 'n' to pass: ") 
            if player_draws == "y":
                player_hand+=draw_card(1)
                player_score = game_status(player_hand, computer_hand)
            else:
                break
                
        computer_hand = computer_plays(computer_hand)
        print(score_game(player_hand, computer_hand))
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            blackjack()
        else:
            keep_playing ==False
        
        

blackjack()

