#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f'{i}')
        if i == 1:
            print('Happy New Year!')
        i -= 1 
        
    

def square_integers(int_list):
    return [i**2 for i in int_list]
        
    

def fizzbuzz():
    for i in range (1, 101):
        if i % 15 == 0:
            print ('FizzBuzz')

        elif i % 5 == 0:
            print ('Buzz')

        elif i % 3 == 0:
            print ('Fizz')

        else:
            print (f'{i}')
    
