# Logical not opeartor:-
"""
--> not operator always gives boolean reslut, if its operator will boolean or non-boolean.
"""

x=not 4>5
print(x)

x=not 5
print(x)

x=not 0
print(x)

x=not 3+4j
print(x)

x=not 0+0j
print(x)

x=not "saurabh" # Empty str result False, Non-empty str result True
print(x)

x=not ""
print(x)

x="ram" and "shyam"
print(x)

x="ram" or "shyam"
print(x)

x=3 and 4>2
print(x)

x=3 and 3+4
print(x)

"""
x=3 and 3=4
print(x) it gives error

x=5
3 and x=4
print(x) it also gives error, we can not use assignment operator.
"""

x=3 and 3==4
print(x)

x=3 or 5/0
print(x)

"""
x=3 and 5/0
print(x) it gives error because 2nd operand evaluate due to and operator.
"""

x=3 and 10/2
print(x)
