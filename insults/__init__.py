import random
def generate_insult():
    insult = random.randrange(5)
    if insult == 1:
        print("BZZZT! Wrong! Try again...")
    elif insult == 2:
        print("Is this the first time or have you always been this bad ?!")
    elif insult == 3:
        print('Why are you so bad at this?')
    elif insult == 4:
        print("I would insult you, but I'm not permitted to insult trash")
    else:
        print("Wow! You are spectacularly horrible at this!!")
