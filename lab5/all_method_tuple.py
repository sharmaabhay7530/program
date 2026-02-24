# Python program to demonstrate tuple operations

# 1️⃣ Creating a tuple
t = (10, 20, 30, 40, 50, 10)
print("Original tuple:", t)
# Output: (10, 20, 30, 40, 50, 10)

# 2️⃣ Access elements
print("First element:", t[0])   # Output: 10
print("Last element:", t[-1])   # Output: 10

# 3️⃣ Slicing
print("Slice t[1:4]:", t[1:4])  # Output: (20, 30, 40)
print("Slice t[:3]:", t[:3])    # Output: (10, 20, 30)

# 4️⃣ Length of tuple
print("Length of tuple:", len(t))  # Output: 6

# 5️⃣ Count occurrences
print("Count of 10:", t.count(10))  # Output: 2

# 6️⃣ Index of element
print("Index of first 30:", t.index(30))  # Output: 2

# 7️⃣ Concatenation
t2 = (60, 70)
t3 = t + t2
print("After concatenation:", t3)
# Output: (10, 20, 30, 40, 50, 10, 60, 70)

# 8️⃣ Repetition
t4 = t * 2
print("After repetition:", t4)
# Output: (10, 20, 30, 40, 50, 10, 10, 20, 30, 40, 50, 10)

# 9️⃣ Reversing a tuple
t_reversed = t[::-1]
print("Reversed tuple:", t_reversed)
# Output: (10, 50, 40, 30, 20, 10)

# 10️⃣ Tuple unpacking
a, b, c, d, e, f = t
print("Unpacked values:", a, b, c, d, e, f)
# Output: 10 20 30 40 50 10

# 11️⃣ Nested tuples
nested = (1, 2, (3, 4, 5), 6)
print("Nested tuple:", nested)
# Output: (1, 2, (3, 4, 5), 6)
print("Access nested element 4:", nested[2][1])
# Output: 4

# 12️⃣ Tuple membership
print("Is 20 in t?", 20 in t)    # Output: True
print("Is 100 not in t?", 100 not in t)  # Output: True