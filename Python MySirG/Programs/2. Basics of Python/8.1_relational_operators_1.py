# Relational Operators always gives 'True' or 'False' as a result:-
x=3>5
print(x)

x=4>=4
print(x)

x=5==4
print(x)

# We can convert 'True' or 'False' in int with the help of type conversion:-
x=True
y=int(x)
print(y)

x=False
y=int(x)
print(y)

x=4
y=bool(x)
print(y)

x=1
y=bool(x)
print(y)

x=0
y=bool(x)
print(y)

"""
Every non-zero value is considered as 'True' and zero value is considered as 'False'
"""

# Relational Operators also works on strings:-
x="AB">"CD"
print(x)

x="ABC"=="DEF"
print(x)

x="AB"=="AB"
print(x)

# Relational Operators also works on complex numbers:-
'3+4j>2+3j It will not work in relational operator'
x=2+3j==3+4j
print(x)

