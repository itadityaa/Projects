import random
max_score = 50

def dice_roll():
    random_number = random.randint(1, 100)
    if random_number <= 25:
        return 1
    else:
        return random.randint(2, 6)

def player_turn(turn_score=0):
    response = input("Would you like to roll the dice? (y/n) ")
    if response.lower() == 'y':
        roll = dice_roll()
        if roll == 1:
            print("You rolled a 1! Your turn is over.")
            return 0
        else:
            turn_score += roll
            print(f"You rolled a {roll}! Your score for this turn is {turn_score}.\n")
            if turn_score >= max_score:
                return turn_score
            return player_turn(turn_score)
    elif response.lower() == 'n':
        print(f"You scored {turn_score} this turn.")
        return turn_score

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
    while max(scores) < max_score:
        for i in range(players):
            print(f"\nPlayer {i + 1}, it's your turn!")
            scores[i] += player_turn()
            
            print(f"\nPlayer {i + 1} your total score is {scores[i]}")
    
    final_score_value, player_number = final_score(scores)
    if final_score_value == 0:
        print("\nNo one wins!")
    else:
        print(f"\nCongratulations!!! Player {player_number} wins with a score of {final_score_value}!")
  
play_game()