"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Eslami Ghayour

email: eslamidaniel@gmail.com

discord: DanielEG eslami.d

"""

import pandas as pd
import numpy as np
import re

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
delimiter = "-" * 40
print('Username:')
user_name_input = input()
print('Password:')
user_password_input = input()
print(delimiter)

register = {
        'user_name_reg': ['bob', 'ann', 'mike', 'liz'],
        'user_password_reg': ['123', 'pass123', 'password123', 'pass123']
                }
reg_users =pd.DataFrame(data=register) #creating a dataframe for registered users

index_of_user = reg_users.loc[reg_users['user_name_reg'] 
                == user_name_input].index.values #searching a user by index


reg_password = reg_users['user_password_reg'].iloc[index_of_user] #searching right password of a user
try:
    if reg_password[0] == user_password_input and user_password_input != '': #making sure, that a password is correct
        print(      'Welcome to the app, ' + user_name_input)
        print(      'We have 3 texts to be analyzed.')
        print(delimiter)
        print(      'Enter a number btw. 1 and 3 to select:')
        print(delimiter)
        selected_number = input()
        
        try:
            choosed_text = TEXTS[int(selected_number) - 1] #user chooses a text
            splitted_text = choosed_text.split()
            number_of_words = len(splitted_text)

            df = pd.DataFrame(splitted_text) #making dataframe

            df['upper'] = df[0].str.findall(r'[A-Z]').str.len()
            uppercase_letters = sum(df['upper']) #counting all uppercase letters
            df['bool_multiupper'] = df['upper'] >= 2 #finding uppercase words
            indexes_multiupper = df.index[df['bool_multiupper'] == True].tolist() 
            count_of_multiupper = len(indexes_multiupper) #number of the uppercase words
            df['upper'] = df[0].str.findall(r'[A-Z][0-9]').str.len() #finding uppercase words and numbers
            numbers_and_upperletters = df[0].str.findall(r'[0-9][A-Z]').str.len() #counting numbers and upper letters
            index_numbers_and_upper = df.index[numbers_and_upperletters == True].tolist() #index of all numbers and upper words
            titlecase_words = (uppercase_letters - 
                               sum(numbers_and_upperletters) - 
                               count_of_multiupper) #counting titlecase words
            
            df['numbers'] = df[0].str.findall(r'[0-9]').str.len() #counting all numbers
            bool_of_str_numbers = df['numbers'] > 0 #finding where are my numbers
            indexes_str_numbers = df.index[bool_of_str_numbers == True].tolist() #finding index of the numbers
            count_of_str_with_numbers = len(indexes_str_numbers) #counting indexes of my numbers
            

            num_df = [] #for future use

            if indexes_str_numbers != 1: #find if we have numbers
                C = 0
                while len(index_numbers_and_upper) > C: # calculating, how many times is loop needed
                    index_in_str_numbers = index_numbers_and_upper[C] #
                    index_index_str_numbers= indexes_str_numbers.index(index_in_str_numbers) # geting index from indexes of numbers 
                    indexes_str_numbers.pop(index_index_str_numbers) #poping the number and upper values
                    C += 1
                else:
                    pass  
                count_of_str_with_numbers = len(indexes_str_numbers) #count of rest numbers
                C = 0 
                while C <= count_of_str_with_numbers - 1: # loop for saving values of numbers
                    value = df[0][indexes_str_numbers[C]] # getting the value of number
                    num_df.append(int(value)) #saving all values in the lsit
                    C += 1
                else:
                    pass
            sum_num =sum(num_df) # summing all

            lowecase = number_of_words - (titlecase_words + count_of_multiupper + count_of_str_with_numbers) 
            #by suming all upper words and numbers and subtracting all words, i get number of lowercase words

            numbers_out = re.sub('[0-9]', '*', choosed_text)
            lowercase_out = re.sub('[a-z]', '*', numbers_out)
            uppercase_out = re.sub('[A-Z]', '*', lowercase_out)
            special_out = re.sub('[,,-]', '*', uppercase_out)
            all_out = re.sub('[.]', '*', special_out) #changing characters to *
            splitted_text = all_out.split() # spliting text to words
            df_word_count = pd.DataFrame(splitted_text)
            

            occurences = df_word_count[0].str.len()
            df_group_by = df_word_count.groupby(occurences).agg(
                            lambda x: x.loc[x.str.len().idxmax()]) #changing order of words
            df_group_by['1'] =df_group_by[0].str.len() #counting the words
            df_group_by.index = np.arange(1, len(df_group_by) + 1) #changing index of df
            
            word_lengths_count = {}

            # for graf
            words = choosed_text.split()
            word_count = len(words)
            for word in words:
                length = len(word.strip('.,'))
                if length in word_lengths_count:
                    word_lengths_count[length] += 1
                else:
                    word_lengths_count[length] = 1


            # printing the result:

            print(  'There are '+ str(number_of_words) +' words in the selected text.\n'
                'There are '+ str(titlecase_words) +' titlecase words.\n'
                'There are '+ str(count_of_multiupper) +' uppercase words.\n'
                'There are '+ str(lowecase) +' lowercase words.\n'
                'There are '+ str(count_of_str_with_numbers) +' numeric strings.\n'
                'The sum of all the numbers '+ str(sum_num)
                )
            print(delimiter)
            print('LEN|     OCCURENCES     |NR.')        
            print(delimiter)
            sorted_lengths = sorted(word_lengths_count.keys())
            for length in sorted_lengths:
                count = word_lengths_count[length]
                graf = '*' * count
                print(f'{length:2} |{graf:20}|{count}')


        except(IndexError):
            print(  'wrong inpout,\ntry harder next time.')
except(KeyError, ValueError):
    print(          'username:' + user_name_input)
    print(          'password:' + user_password_input)
    print(          'unregistered user, terminating the program..')
  
# the end


