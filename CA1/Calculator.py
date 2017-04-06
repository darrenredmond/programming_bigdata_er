import math

#class Calculator(object):
def welcome():
    print(''' Welcome to Emma's Calculator''')
    

def add(first, second):
    return first + second 

def subtract(first, second):
    return first - second 
		
def multiply (first, second):
    return first * second 
		
def divide (first, second):
    response = None 
    if second == 0:
        response = 'error'
    else: 
        return first/float(second)
    return response
		
def exponent (first, second):
    number_types = (int, long, float, complex)
    if isinstance (first, number_types):
        return first ** second 
    else:
        print 'Error'

def square_root (first):
    return math.sqrt(first)

def sin (first):
    return math.sin(first)

def cos(first):
    return math.cos(first)

def tan(first):
    return math.tan(first)

def factorial(first):
    return math.factorial(first)
            

			


		
	