# Week 2 - Assignment 1: Finding your dog’s age relative to you
# Create a program that asks for user input their first name, last name and birth year. Based on
# the input you should display the user’s full name, initials and the calculated age in human
# and dog years (The formula for calculating age in dog years is age(in human years) * 7 )
    # Step 1 : Create a new python file and name it dog_years.py in your existing project (If you
    # don’t have a project, then create a new project and then create a python file)
    # Step 2 : Use the input function to ask for the user’s first name and last name and store them
    # in two variables, first_name and last_name.
    # Step 3 : Print a greeting for the user that says “Hello full_name!!” where full_name is
    # replaced full_name that you construct using the first_name and last_name variables.
    # Step 4 : Display the initials of the user by printing “Your initials are ___”.
    # Step 5 : Use the input function to ask for the user’s birth year and store it in a variable
    # called birth_year. Also create a variable called current_year and store 2020 in it.
    # Step 6 : Calculate the age of the user by using his birth year and current year.
    # Step 7 : Calculate the age in dog years and store it in a variable named dog_years.
    # (Remember the formula for calculating age in dog years is to multiply the age in
    # human years by 7.)
    # Step 8 : Print the user’s age in both human years and dog years along with an appropriate
    # print message.

#Ask User for input = Age in dog years, Birth_name, Last name
First_name = input('Please enter your first name:')
Last_name = input('Please enter your last name:')
Age = int(input('Please enter your birth year:'))
Full_name = First_name + Last_name
Current_year = 2020
Dog_Years = (Current_year - Age) * 7
print('Hello!', Full_name)
print('Your age in dog years is', Dog_Years)