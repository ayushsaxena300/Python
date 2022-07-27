# Assignment Operators:-
x=4
print(x)

"""
4=x
3=4
We can not assign like this, it will gives error.
Always right value store in left.
Left operand of assignment operator will always be variable.

y=y+3
print(y)
It will also gives error because there is no initialization in y.
After initialized value to y it will work properly.
"""
y=5
y=y+3
print(y)

x=5
x+=3
print(x)

x/=2
print(x)

x=5
x*=3+4 # Here operators work accocrding to precedence.
print(x)

x=5
x=x*3+4 # Here also operators work accocrding to precedence.
print(x)
