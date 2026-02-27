# 5️⃣ Mini Challenge: Lists

# -------------------------------
# Normal Case:
# Create a list of 5 integers and print their sum.
# -------------------------------
numbers = [1, 2, 3, 4, 5]
print("Normal Case - Sum of numbers:", sum(numbers))


# -------------------------------
# Edge Case:
# Handle empty list gracefully when trying to access an element.
# -------------------------------
names = []
if names:
    print("Edge Case - First element:", names[0])
else:
    print("Edge Case - List is empty")


# -------------------------------
# Broken Input:
# Try to remove an item not in the list and handle the exception.
# -------------------------------
try:
    numbers.remove(6)  # 6 is not in the list
except ValueError:
    print("Broken Input - Item not found in the list")