"""
Mini Project: Weight Converter
"""

weight = float(input("Enter Weight: "))
unit = input("(K)g or (L)bs: ").strip().upper()

if unit == "L":
    result = weight * 0.453592
    print(f"Weight in Kg: {round(result, 2)}")
elif unit == "K":
    result = weight / 0.453592
    print(f"Weight in lbs: {round(result, 2)}")
else:
    print("Invalid unit! Please enter 'K' or 'L'.")