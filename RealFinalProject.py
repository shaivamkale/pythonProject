import random
import insults
turns = 3
Ask_User = input('Do you wish to start with three turns or test your luck with more?(three/rolladice):').lower()

if Ask_User == 'three':
    print('Ok. You have',turns,'turns(s) left. Use them wisely!')
    turns = 3
elif Ask_User == 'rolladice':
    dice_roll = random.randrange(1,6)
    turns = dice_roll
    if dice_roll >= 3:
        print('Luck and fortune are on your side. You have',turns,'turn(s) left.')
    elif dice_roll < 3:
        print('Luck was not on your side. You have',turns,'turn(s) left.')



while turns != 0:
    lucky_guess_ai = random.randrange(0, 11)
    user_answer = int(input('Enter a number between 0 and 11:'))
    if user_answer == lucky_guess_ai:
        print('Congratulations! You won!')
        break
    elif user_answer != lucky_guess_ai:
        print('The magic number was',lucky_guess_ai)
        insults.generate_insult()
        turns = turns - 1
if turns == 0:
    print('Game Over.')
    exit(0)
