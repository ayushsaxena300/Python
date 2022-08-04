# importing module:-
'''
factorial(5) It will gives error, we need to use import math module first.
'''

import math
print(math.factorial(5))

import math
print(math.sqrt(25))

help(math) # This is how we know the functions present in math module

'''
import math
print(math.factorial(-4))
factorial() function is not valid for negative and non-integral values.
'''

import math as m # Here we use alias name with the help of 'as' keyword
print(m.factorial(5))

'''
print(math.factorial(4)) After using alias name we can not use other name.
'''

# from keyword:-
from math import factorial
print(factorial(5)) # Here we don't need to write module name

'''
print(math.factorial(5)) After using from keyword we can not use module name.
'''

'''
from math import factorial,sqrt
with this we can use differnt-different functions
'''

from math import * # To use all functions of a module we use *
print(gcd(6,4))
print(sqrt(25))
