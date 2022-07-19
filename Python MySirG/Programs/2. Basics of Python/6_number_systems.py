# Decimal Number
x=45
print(x)

# Binary Number
x=0b101
print(x)

x=0B101
print(x)

# Octal Number
x=0o10
print(x)

x=0O10
print(x)

# Hexa-decimal Number
x=0x3f
print(x)

x=0X3f
print(x)

# Print the value of binary, octal, hexa-decimal number as it is:-
x=0x3f
print(hex(x)) # It print(return) binary, octal, hexa-decimal as a srting

x=0o10
print(oct(x))

x=0b101
print(bin(x))

y=bin(x) # With the help of 'slicing' we remove '0b' from preffix:-
print(y[2::])
