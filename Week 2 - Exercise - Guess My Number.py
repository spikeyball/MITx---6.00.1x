# Exercise: guess my number
# 10.0/10.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 15 minutes
#
# In this problem, you'll create a program that guesses a secret number!
#
# The program works as follows: you (the user) thinks of an integer between 0
# (inclusive) and 100 (not inclusive). The computer makes guesses, and you give
# it input - is its guess too high or too low? Using bisection search, the
# computer will guess the user's secret number!
#
# Here is a transcript of an example session:
#
# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 81?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 84?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 82?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83
# Important
# Hint: Endpoints
# Python Trick: Printing on the same line
# Click to See Test Cases
#
# Note: your program should use input to obtain the user's input! Be sure to
# handle the case when the user's input is not one of h, l, or c.
#
# When the user enters something invalid, you should print out a message to the
# user explaining you did not understand their input. Then, you should re-ask the
# question, and prompt again for input. For example:
#
# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. y
# Sorry, I did not understand your input.
# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
# too low. Enter 'c' to indicate I guessed correctly. c

low = 0
high = 100
mid = int((high - low) / 2)

print('Please think of a number between 0 and 100!')
print('Is your secret number {0}?'.format(mid))
letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while letter != 'c':
    if letter == 'h':
        high = mid
        mid = int((high + low) / 2)
    elif letter == 'l':
        low = mid
        mid = int((high + low) / 2)
    else:
        print('Sorry, I did not understand your input')
    print('Is your secret number {0}?'.format(mid))
    letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print('Game over. Your secret number was: {0}'.format(mid))
