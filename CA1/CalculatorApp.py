from Calculator import *

print welcome ()

while True:
    operator = raw_input('''
    Please type in the operation you would like to complete:
    +  for Addition
    - for Subtracion
    * for Multiplication
    / for Division
    ** for Exponent
    sqrt for Square root
    sin for Sin 
    cos for Cos
    tan for Tan
    ''')

    
    first = input('Please input your fist number:\n  ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':
        second= input('Please input your second number:\n  ')


    if operator == '+':
        result = add(first,second)
    elif operator == '-':
        result = subtract(first,second)
    elif operator == '*':
        result = multiply(first,second)
    elif operator == '/':
        result = divide(first, second)
    elif operator == '**':
        result = exponent(first,second)
    elif operator == 'sqrt':
        result = square_root(first)
    elif operator == 'sin':
        result = sin(first)
    elif operator == 'cos':
        result = cos(first)
    elif operator == 'tan':
        result = tan(first)
    elif operator == '!':
        result = factorial(first)
    else:
        print ('Sorry you have not inputes a valid operator')
        continue
        
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':  
       print result 
        
    else:
        print result #'{} {} is equal to: {}'.format(operator,first,result)

    repeat_calc = raw_input('''
    Would you like to calculate again?
    Please type Y for Yes and N for No
    ''')
    if repeat_calc == 'N':
        print 'Goodbye'
    else:
        continue 