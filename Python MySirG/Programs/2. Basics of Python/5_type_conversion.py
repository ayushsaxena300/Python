x=5
print(type(x))
x=3.4
print(type(x))
x="123"
print(type(x))

# Type Conversion
x="123"
y=5
print(int(x)+y) # Here print(x+y) gives us error, so we convert sring "123" in integer by using int(x) function.

# int() type conversion
x="123"
y=int(x)
print(type(y))

x=3.5
y=int(x)
print(type(y))
print(y)

# str() type conversion
x=123
y=str(x)
print(type(y))

# ord() type conversion (unicode)
x='a'
y=ord(x)
print(y)
