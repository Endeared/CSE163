# Ross Hamey
# CSE163 - Mini Project 3, Updated
# 11/19/2023
# https://github.com/Endeared
# no recording for this assignment (out of town)

# updated based on feedback from Michael Connaughton (see line 123 & comments)

# random import
import random as rand

'''
playAgainPrompt function, which takes in a target, bet, and result (won or lost),
and returns a string of either 'y' or 'n' depending on the user's input
'''
def playAgainPrompt(target, bet, result):
    # formatting our bet to two decimal places, displaying prompt
    bet = "{:.2f}".format(bet)
    play_again = input(f'You rolled a {target} and {result} ${bet}. Do you want to play again (y/n)? ')

    # while loop to ensure user enters a valid option
    valid = False
    while not valid:
        if play_again == 'y' or play_again == 'n':
            valid = True
            return play_again
        else:
            play_again = input("Please enter a valid option (y/n): ")

'''
roll function, which returns the sum of two random integers between 1 and 6
'''
def roll():
    # rolling dice and returning sum
    dice1 = rand.randint(1, 6)
    dice2 = rand.randint(1, 6)
    return dice1 + dice2

'''
promptUser function, which prompts the user for a bet and returns the bet
'''
def promptUser():
    # while loop to ensure user enters a valid bet
    valid_bet = False 
    while not valid_bet:
        try:
            bet = float(input("How much would you like to bet? "))
            # making sure bet is not less than the lowest denomination of currency
            if bet <= 0.01:
                print("Please enter a valid bet (greater than $0.01).")
                continue
            else:
                return bet
        except:
            print("Please enter a valid bet.")
            continue

'''
main function, which simply runs the game with the user of our helper functions
'''
def main():
    # setting initial game variables
    play_again = ''
    count = 0
    total = 0

    # while loop to keep playing until user enters 'n'
    while play_again != 'n':
        # incrementing count for each game, prompting for bet, and doing first roll
        count += 1
        bet = promptUser()
        target = roll()

        # checking for win / loss conditions on first roll, calling playAgainPrompt
        # function accordingly. increment / decrement total accordingly
        if target == 7 or target == 11:
            play_again = playAgainPrompt(target, bet, 'won')
            total += bet
        elif target == 2 or target == 3 or target == 12:
            play_again = playAgainPrompt(target, bet, 'lost')
            total -= bet
        # otherwise, we start our process of rolling 1 or more times until we hit
        # a winning or losing condition
        else:
            # while loop to keep rolling until we hit a win / loss condition, also
            # copying our target to a variable called current_roll to keep track of
            # our current roll
            keep_rolling = True
            current_roll = target
            while keep_rolling:
                # prompting user to roll again, and making sure they press enter
                rolling = input(f'You rolled a {current_roll}. Press the Enter key to roll again. ')
                valid = False
                while not valid:
                    if rolling == '':
                        valid = True
                    else:
                        rolling = input("Please press the Enter key to roll again. ")
                
                # rolling again, checking for win / loss conditions, and calling
                # playAgainPrompt function accordingly. we also increment / decrement
                # the total accordingly
                result = roll()
                if result == target:
                    play_again = playAgainPrompt(result, bet, 'won')
                    total += bet
                    keep_rolling = False
                elif result == 7:
                    play_again = playAgainPrompt(result, bet, 'lost')
                    total -= bet
                    keep_rolling = False
                # otherwise, if no win or loss condition is met, we simply update
                # our current roll value
                else:
                    current_roll = result
    
    # once the user has entered 'n', we format our total to two decimal places as
    # a separate var, then check which condition our total satisfies and print
    # accordingly
    # extra point / revised change - added a abs() call and supplied my total to
    # ensure that the display is not improper (i.e now if you lost money it will
    # display that you "lost a total of $x.xx" instead of "los a total of $-x.xx")
    total_str = "{:.2f}".format(abs(total))
    if total > 0:
        print(f'You played {count} games and won a total of ${total_str}.')
    elif total < 0:
        print(f'You played {count} games and lost a total of ${total_str}.')
    else:
        print(f'You played {count} games and broke even.')

# calling main function and input to keep window open if ran from IDLE
# (and not a terminal or powershell window)
if __name__ == "__main__":
    main()
    input()
    


