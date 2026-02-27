# ================================
# Loop Practice Exercises
# ================================

# -------------------------------
# 1️⃣ For Loop: iterate over a list
# -------------------------------
numbers = [1, 2, 3, 4, 5, 6]
for item in numbers:
    print("For Loop - item:", item)


# -------------------------------
# 2️⃣ While Loop: iterate using index
# -------------------------------
i = 0
while i < len(numbers):
    print("While Loop - item:", numbers[i])
    i += 1


# -------------------------------
# 3️⃣ Simple For Loops on different iterables
# -------------------------------
# List
numbers2 = [1, 2, 3]
for n in numbers2:
    print("List iteration:", n)

# String
for ch in "Python":
    print("String iteration:", ch)

# Tuple
for t in (1, 2, 3):
    print("Tuple iteration:", t)


# -------------------------------
# 4️⃣ Using range() in For Loops
# -------------------------------
for i in range(5):  # 0 → 4
    print("Range(5):", i)

for i in range(2, 10, 2):  # start, stop, step
    print("Range(2,10,2):", i)


# -------------------------------
# 5️⃣ Nested For Loops
# -------------------------------
for i in range(3):
    for j in range(2):
        print("Nested Loop:", i, j)


# -------------------------------
# 6️⃣ For Loop with break and else
# -------------------------------
for n in range(3):
    if n == 2:
        break
else:
    print("Loop completed")  # won't run because break executed


# -------------------------------
# 7️⃣ While Loop countdown
# -------------------------------
i = 3
while i > 0:
    print("Countdown:", i)
    i -= 1