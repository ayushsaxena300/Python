# Membership Operators:-
x="abc"
print("a" in x)
print("A" in x)
print("A" not in x)

"""
x=256
print(5 in x)
It will gives error because,
It is not iterable(collection of values), it is a single value.
"""

x=[10,20,30] # It is iterable because it is List
print(20 in x)

x=1,2,3,4
print(4 in x) # It is iterable because it is Tuple

x="MySirG.com"
print("My" in x)
print("Sir" in x) # We can also check sub-string with the help of 'in' and 'not in' operators
