# Project available at https://hyperskill.org/projects/175

import random

if __name__ == '__main__':
    n = int(input('Enter the number of friends joining (including you): '))

    names_dictionary = {}
    if n <= 0:
        print()
        print('No one is joining for the party')
    else:
        print()
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(n):
            names_dictionary[input()] = 0
        print()

        total_bill_split = int(input("Enter the total bill value: ")) / n  
        total_bill_split = round(total_bill_split, 2)
        print()

        names_dictionary = names_dictionary.fromkeys(names_dictionary, total_bill_split)

        print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

        user_input = str(input())
        
        if user_input == 'Yes':
            list_names = list(names_dictionary.keys())
            lucky_user = random.choice(list_names)
            print()
            print(lucky_user, "is the lucky one!")
            total_bill_split = total_bill_split * n / (n - 1) 
            total_bill_split = round(total_bill_split, 2)
            names_dictionary = names_dictionary.fromkeys(names_dictionary, total_bill_split)
            names_dictionary[lucky_user] = 0
            print()
            print(names_dictionary)
            
        if user_input == 'No':
            print()
            print("No one is going to be lucky")
            print()
            print(names_dictionary)
        