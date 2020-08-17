import random as r
def odd_num_filter(num):
    TestEmpty = []
    for x in range(0,10):
        y = r.randrange(0,num)
        TestEmpty.append(y)
    for x in TestEmpty:
        if x%2 != 0:
            print(x,'is an odd number.')
        else:
            print(x,'is an even number.')
    return
num = int(input("Enter random number:"))
odd_num_filter(num)

