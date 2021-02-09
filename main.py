from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


##Calculate point amount
def calculate_score(hand):
  """take list of card within hand, and return score"""
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)


##Compare computer and user score
def compare(user_cards, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, computer has Blackjack"
  elif user_score == 0:
    return "Win, Blackjack"
  elif user_score > 21:
    return "Lose, over 21"
  elif computer_score > 21:
    return "Win, computer over 21"
  elif user_score > computer_score:
    return "Win, closer to 21 than computer"
  else:
    return "You lose"


play = True

want_to_play = input("Do you want to play Blackjack? Type 'y' or 'n': ")

while play:
  game_continue = True

  user_hand = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
  computer_hand = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
  
  user_score = int(calculate_score(user_hand))
  computer_score = int(calculate_score(computer_hand))
  print(f"  Your cards: {user_hand}, current score: {user_score}")
  print(f"  Computer's first card: {computer_hand[0]}")

  while game_continue:  
    if user_score > 21 or user_score == 0 or computer_score == 0:
      game_continue = False 
    
    else:
      ## Should Computer take another card ?
      while computer_score < 17 and computer_score != 0:
        computer_hand.append(cards[random.randint(0, 12)])
        computer_score = calculate_score(computer_hand)
      
      ## Want user an other card ?
      add_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if add_card == 'y':
        user_hand.append(cards[random.randint(0, 12)])
        user_score = int(calculate_score(user_hand))
        print(f"  Your cards: {user_hand}, current score: {user_score}")
      else:
        game_continue = False
        
  print(compare(user_score, computer_score))

  print(f"  Your hand: {user_hand}, your score: {user_score}\n  Computer hand: {computer_hand}, Computer score: {computer_score}")

  want_to_play = input("Do you want to play Blackjack again? Type 'y' or 'n': ")

  if want_to_play == "n":
    play = False
    clear()
    print("Have a nice day! 🧚")
