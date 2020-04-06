import random

print('Iam thinking of a number between 20 and 30')

secretnum = random.randint(20,30)

for guesses in range(6):
    print('Take a guess..')
    num = int(input())
    if num>secretnum:
        print('Your guess is too high!')
    elif num<secretnum:
        print('Your num is too low!')
    else:
        break

if num == secretnum:
    print('CORRECT,You guessed in {} attempts'.format(guesses))

else:
    print('You have failed, iam thinking of ',secretnum)
