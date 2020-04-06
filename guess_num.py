import random
print('Iam thinking of a number between 10 and 20, take a guess')

global x
x = 0
secretnum = random.randint(10,20)
while True:
    num = int(input())
    if num > secretnum:
        print('Your guess is too high')
        print('Take a guess')
        x += 1
        
    elif num < secretnum:
        print('Your guess is too low')
        print('Take a guess')
        x += 1

    elif num == secretnum:
        print('Correct! You guessed in {} attempts'.format(x))
