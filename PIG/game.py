import random
max_score = 50

def dice_roll():
    random_number = random.randint(1, 100)
    if random_number <= 5:
        return 1
    else:
        return random.randint(2, 6)

def player_turn(current_score = 0):
    response = input("Would you like to roll the dice? (y/n) ")
    if response.lower() == 'y':
        roll = dice_roll()
        if roll == 1:
            print("You rolled a 1! Your turn is over.")
            return 0
        else:
            current_score += roll
            print(f"You rolled a {roll}! Your score for this turn is {current_score}.\n")
            if current_score >= max_score:
                return current_score
            return player_turn(current_score)
    elif response == 'n':
        print(f"You scored {current_score} this turn.")
        return current_score

def win_check(scores, max_score):
    for i in range(len(scores)):
        if scores[i] >= max_score:
            return True, i + 1
    return False, None

def final_score(scores):
    max_score = max(scores)
    if max_score == 0:
        return 0, 0
    player_number = scores.index(max_score) + 1
    return max_score, player_number

def play_game():
    while True:
        players = int(input("How many players? Enter a number less than 5: "))
        if players > 4:
            print("Too many players!")
        else:
            if players <= 1:
                print("You can't play this game alone!")
            else:
                break
    
    scores = [0] * players
    print("The first player to reach 100 points wins!")
    print("Let's play!")
    for i in range(players):
        print(f"\nPlayer {i + 1}, it's your turn!")
        scores[i] += player_turn()
        win_condition, player_number = win_check(scores, max_score)
        if win_condition:
            # print(f"\nPlayer {player_number} wins! with a score of {scores[i]}")
            break
        print(f"\nPlayer {i + 1} your total score is {scores[i]}")
    
    final_score_value, player_number = final_score(scores)
    if final_score_value == 0:
        print("\nNo one wins!")
    else:
        print(f"\nCongratulations!!! Player {player_number} wins with a score of {final_score_value}!")
  
play_game()