import random
import time

def guessing_game():
    low = 1
    high = 10
    guess = ''
    target = random.randint(low,high)
    print(target)
    error = f'Pick a number between {low} and {high}:\n'))


    while guess != target:
        guess = input(f'Pick a number between {low} and {high}:\n')
        if guess.isdigit():
            guess = int(guess)
            if guess > target:
                print('guess too high')
            elif guess < target:
                print('guess too Low')
            else:
                print(f"Ding Ding Ding, You are correct! the target was {target}")
        else:
            print('please enter a number:')


def al_guessing(target=7,high=10):
    low = 1
    guess = 0
    guess_ct = 0
    print(target)

    while guess != target:
        guess = random.randint(low, high)
        guess_ct += 1
        print(f'I Guess ..... {guess}')
        if guess > target:
            high = guess-1
            print('(too high)')
        elif guess < target:
            low = guess+1
            print('(too low)')
        else:
            print('Nice!!')
            print(f'it took {guess_ct} guesses')

        time.sleep(1)
    return guess_ct



if __name__ == '__main__':
    # guessing_game()
    al = {}
    highs = [10,100,1000,10000]
    targets = [7,26,713,4587]
    for i in range(len(highs)):
        al[i] = al_guessing(high=highs[i])

    print(al)