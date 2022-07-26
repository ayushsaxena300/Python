# Logical Operators
x=3>4 and 5>3 # Result will always 'False' if first operand is 'False' in "and" operator
print(x)

x=3!=4 and 10<20
print(x)

x=4>3 or 3<2 # Result will always 'True' if first operand is 'True' in "or" operator
print(x)

# Logical and opeartor:-
"""
--> x and y
--> if x and y are non-boolean then result is also non-boolean.
--> if x is False then result is x; otherwise y.
"""
x=5 and 4
print(x)

x=0 and 4
print(x)

x=3 and 5
print(x)

x=3 and 3.4
print(x)

x=3 and "ab"
print(x)

# logical or operator:-
"""
--> x or y
--> if x or y are non-boolean then result is also non-boolean.
--> if x is False then result is y; otherwise x.
"""
x=3 or 4
print(x)

x=0 or 5
print(x)

x=0 or False
print(x)

x=3 or False
print(x)

