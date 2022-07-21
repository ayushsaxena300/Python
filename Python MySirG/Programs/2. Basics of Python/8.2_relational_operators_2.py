# Boolean Type values can operates with int and float:-
x=True+5
print(x)

x=True+3.5
print(x)

# Chaining of operators:-
x=5>4>3
print(x)

x=5>4>3>2>1
print(x)

x=5>4>3>2<1
print(x)

# Comparison between str and int:-
x=3+4j==3+4j
print(x)

x=5=="5"
print(x)

x='a'==97 # For equality operator(== or !=) it will check content as well as type
print(x)

x='a'==97
y=ord('a')==97
print(y)

"""
x="a">5 - It gives error because there is no comparison between str and int,
print(x)  we can compare it with the help of equality operator i.e(== or !=).
"""


# Comparison between float and int:-
x=5==5.0 # Comparison between int and float is possible because it is exception
print(x)

x=5=="5"
print(x)

# Comparison between boolean and int:-
x=True==1
print(x)

x=True==5
print(x)

x=5<6.5
print(x)

x=True!=False
print(x)
