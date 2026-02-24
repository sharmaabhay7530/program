
# 1️⃣ Create a set
s = {10, 20, 30, 40, 50, 10}
print("Original set:", s)  
# Output: {10, 20, 30, 40, 50}  (duplicates removed automatically)

# 2️⃣ add()
s.add(60)
print("After add(60):", s)
# Output: {10, 20, 30, 40, 50, 60}

# 3️⃣ update()
s.update([70, 80, 90])
print("After update([70,80,90]):", s)
# Output: {10, 20, 30, 40, 50, 60, 70, 80, 90}

# 4️⃣ remove()
s.remove(30)
print("After remove(30):", s)
# Output: {10, 20, 40, 50, 60, 70, 80, 90}

# 5️⃣ discard()
s.discard(100)  # No error even if 100 not present
print("After discard(100):", s)
# Output: {10, 20, 40, 50, 60, 70, 80, 90}

# 6️⃣ pop() - removes random element
popped = s.pop()
print("Popped element:", popped)
print("Set after pop():", s)
# Output: Popped element: (random), Set after pop(): (remaining elements)

# 7️⃣ copy()
s_copy = s.copy()
print("Copied set:", s_copy)
# Output: Copy of set

# 8️⃣ Mathematical operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("s1:", s1)
print("s2:", s2)

print("Union (s1 | s2):", s1 | s2)
# Output: {1, 2, 3, 4, 5, 6}

print("Intersection (s1 & s2):", s1 & s2)
# Output: {3, 4}

print("Difference (s1 - s2):", s1 - s2)
# Output: {1, 2}

print("Symmetric difference (s1 ^ s2):", s1 ^ s2)
# Output: {1, 2, 5, 6}

# 9️⃣ isdisjoint()
s3 = {7, 8}
print("s1 is disjoint with s3:", s1.isdisjoint(s3))
# Output: True

# 10️⃣ issubset() and issuperset()
print("s1 is subset of s2:", s1.issubset(s2))
# Output: False

print("s2 is superset of {3,4}:", s2.issuperset({3,4}))
# Output: True

# 11️⃣ clear()
s3.clear()
print("s3 after clear():", s3)
# Output: set()