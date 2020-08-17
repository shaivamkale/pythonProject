'''
shares = int(input('How many shares do you wish to purchase?'))
shares_cost = shares * 32.87
commision1 = shares_cost * 0.02
costwithcommision = float(shares_cost + commision1)
print('These shares cost',shares_cost)
print('The broker commission is', commision1)
print('The total cost is %.3f' % costwithcommision)

shares_cost2 = shares * 33.92
commision2 = shares_cost2 * 0.02
costwithoutcommision = float(shares_cost2 - commision2)
print('You sold these shares for a total value of', shares_cost2)
print('The broker commission is', commision2)
print('You made %.3f' % costwithoutcommision)
profit=costwithoutcommision-costwithcommision
print('Final Outcome:',profit)
if profit < 0:
    print('You lost money on this sale. ;-;')
elif profit == 0:
    print('You made no money :(')
else:
    print('You made profit :)')
'''
inputyear= int(input("Enter the year..."))
def population(inputyear):
    digit_year = inputyear % 100
    leapyear = ((inputyear - 2005) // 5) + 1
    print(leapyear)
    Difference = ((digit_year - leapyear) / 10) + 6
    return Difference
result = population(inputyear)
print('This is the world population:', result)

