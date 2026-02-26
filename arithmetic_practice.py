"""
Topic: Arithmetic Operations
"""

x = 10
x = 10 + 10
x += 5
y = 2
z = -5
zz = "12"
z1 = 0

print("x:", x)
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x ** y:", x ** y)
print("x / y:", x / y)
print("x // y:", x // y)
print("String to int:", int(zz) + x)

try:
    print("Divide by zero:", x / z1)
except ZeroDivisionError:
    print("Cannot divide by zero")