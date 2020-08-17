import random
print('Welcome to Lucky Draw! Here you pick a number in the specified range and get a prize for getting it right! Good Luck!')
#Uinput = int(input('Enter a number between 1 and 10:'))
#Draw = random.randrange(1,10)
count = 0
for count in range(0,3):
    count += 1
    Uinput = int(input('Enter a number between 1 and 10:'))
    Draw = random.randrange(1, 10)
    if Uinput == Draw:
        print('You get',10*Draw, 'dollars. Nice job!')
        break
    elif Uinput == Draw - 1:
        print('The number was:', Draw)
        print('You get 10 dollars for being close.')
        break
    elif Uinput == Draw + 1:
        print('The number was:', Draw)
        print('You get 10 dollars for being close.')
        break
    elif Uinput < 1:
        print('This is not a valid number. Please enter a valid number.')
    elif Uinput > 10:
        print('This is not a valid number. Please enter a valid number.')
    else:
        print('The number was:', Draw)
        print('Try again next time!')
