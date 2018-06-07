import constant

print("Hello world!")

print("Constant Printing ")

print(constant.PI)
print(constant.GRAVITY)

#for Loop
print("\nFor Loop")
for i in range(1,11):
    print(i)
    if i == 5:
        break

# Assigning multiple values to multiple variables
print("\nAssigning multiple values to multiple variables")
a, b, c = 5, 3.2, "Hello"
print (a)
print (b)
print (c)

"""Function to double the value Comment Style"""
print("\n Same value multiple variables")
x = y = z = "same"
print (x)
print (y)
print (z)

print ("\n Printing Literals ")
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# Python contains one special literal i.e. None. We use it to specify to that field that is not created.