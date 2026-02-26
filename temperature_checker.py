"""
Topic: If-Elif-Else Conditionals
"""

temp = int(input("Enter Temperature: "))

if temp > 30:
    print("It's Hot")
    print("Drink chilled drink")
elif temp < 5:
    print("It's a cold day")
    print("Wear a jacket")
elif 10 <= temp <= 30:
    print("It's a beautiful day")
else:
    print("It is cold")