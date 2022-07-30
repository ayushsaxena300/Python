# Identity Operators:-
x=5
y=5
print(x==y)
print(x is y)# Here x and y refers to same variables so value is True

y=6
print(x==y)
print(x is y)# Here x and y refers to different variables so value is False

x=5
y=5.0
print(x==y)
print(x is y)
"""
Here content is same but they point different-different memory location,
because type is different so, 'is' gives us 'False' result.
"""

print(x is not y)
