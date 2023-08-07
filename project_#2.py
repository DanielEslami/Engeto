"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Eslami Ghayour

email: eslamidaniel@gmail.com

discord: DanielEG eslami.d

"""

print(  'Hi there!\n'
        '-----------------------------------------------\n'
        'I\'ve generated a random 4 digit number for you.\n'
        'Let\'s play a bulls and cows game.\n'
        '-----------------------------------------------\n'
        'Enter a number:\n'
        '-----------------------------------------------')

import random
from random import choice
x = 0 # number of tries
number_1 = random.randint(1,9) #generating random numbers with exceptions
number_2 = choice([i for i in range(0,9) if i not in [number_1]])
number_3 = choice([i for i in range(0,9) if i not in [number_1,number_2]])
number_4 = choice([i for i in range(0,9) if i not in [number_1,number_2, number_3]])
numbers = (number_1, number_2, number_3, number_4) #puting them together
numbers = list(numbers) #making list


while True: #infinite loop, it ends only, when you win the game
    input_numbers = input() 
    bulls = 0
    cows = 0
    if len(input_numbers) != 4 or not input_numbers.isnumeric():
        #making sure,that user, puts in the right numbers
        print('try it again.\n Please this time, try it correctly.')
        continue
    else:
        pass

    
    try:
        for a in range(0,4): #finding out bulls
            if numbers[a] == int(input_numbers[a]):
                bulls += 1
        else:
            pass
    except(ValueError): 
        # just for sure, if user would put something else than letter or number
        print('Please enter numbers, not anything else.')

        
    for e in range(0,4): #cascade of cows searching
        if numbers[0] == int(input_numbers[e]):
            if numbers[e] != int(input_numbers[e]):
                cows += 1
            else:
                pass
        else:
            pass
    for i in range(0,4):
        if numbers[1] == int(input_numbers[i]):
            if numbers[i] != int(input_numbers[i]):
                cows += 1
            else:
                pass
        else:
            pass
    for o in range(0,4):
        if numbers[2] == int(input_numbers[o]):
            if numbers[o] != int(input_numbers[o]):
                cows += 1
            else:
                pass
    else:
        pass
    for u in range(0,4):
        if numbers[3] == int(input_numbers[u]):
            if numbers[u] != int(input_numbers[u]):
                cows += 1
            else:
                pass
    else:
        pass
    if bulls == 4: #if he wins...
        print('Correct, you\'ve guessed the right number\n'
        'in ' + str(x) + ' guesses!')
        break
    else:
        pass #many many printing of answers because of english...
    if bulls >= 2 and cows == 1:
        print(str(bulls)+' bulls, 1 cow')
    else:
        pass
    if bulls >= 2 and cows == 0:
        print(str(bulls)+' bulls, 0 cow')
    else:
        pass
    if bulls == 1 and cows == 1:
        print('1 bull, 1 cow')
    else:
        pass
    if bulls == 0 and cows == 1:
        print('0 bulls, 1 cow')
    else:
        pass
    if bulls == 1 and cows == 0:
        print('1 bull, 0 cows')
    else:
        pass
    if bulls == 1 and cows >= 2:
        print('1 bull, '+str(cows)+' cows')
    else:
        pass
    if bulls == 0 and cows >= 2:
        print('0 bull, '+str(cows)+' cows')
    else:
        pass
    if bulls == 0 and cows == 0:
        print('0 bulls, 0 cows')
    else:
        pass
    if bulls >= 2 and cows >= 2:
        print(str(bulls)+' bulls, '+str(cows)+' cows')
    else:
        pass
    x += 1 #counting the tries
else:
    pass