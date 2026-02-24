# -----------------------------------------------------------------------------------------
# 1️⃣ List Practice (10 programs)
# 1. Create a list and print it
numbers = [10, 20, 30, 40, 50]
print(numbers)
# Output: [10, 20, 30, 40, 50]


# 2. Access elements by index
print(numbers[0], numbers[-1])
# Output: 10 50


# 3. Add elements to a list
numbers.append(60)
print(numbers)
# Output: [10, 20, 30, 40, 50, 60]



# 4. Insert element at a position
numbers.insert(2, 25)
print(numbers)
# Output: [10, 20, 25, 30, 40, 50, 60]




# 5. Remove an element
numbers.remove(40)
print(numbers)
# Output: [10, 20, 25, 30, 50, 60]




# 6. Pop last element
last = numbers.pop()
print("Popped:", last, numbers)
# Output: Popped: 60 [10, 20, 25, 30, 50]



# 7. Slice list
print(numbers[1:4])
# Output: [20, 25, 30]




# 8. Reverse list
numbers.reverse()
print(numbers)
# Output: [50, 30, 25, 20, 10]



# 9. Sort list
numbers.sort()
print(numbers)
# Output: [10, 20, 25, 30, 50]



# 10. Sum and average
print("Sum:", sum(numbers), "Average:", sum(numbers)/len(numbers))# Output: [10, 20, 25, 30, 50]
# Output: Sum: 135 Average: 27.0


# ------------------------------------------------------------------------------------------------------------

# 2️⃣ Tuple (10 programs)
# 1. Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
# Output: ('apple', 'banana', 'cherry')



# 2. Access tuple elements
print(fruits[1], fruits[-1])
# Output: banana cherry



# 3. Tuple slicing
print(fruits[0:2])
# Output: ('apple', 'banana')




# 4. Tuple concatenation
t2 = ("orange", "kiwi")
t3 = fruits + t2
print(t3)
# Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi')



# 5. Tuple repetition
print(fruits * 2)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')



# 6. Check element existence
print("banana" in fruits)
# Output: True



# 7. Length of tuple
print(len(fruits))
# Output: 3



# 8. Count occurrences
t4 = (1,2,2,3,2)
print(t4.count(2))
# Output: 3



# 9. Index of element
print(fruits.index("cherry"))
# Output: 2



# 10. Nested tuple
nested = (1, 2, (3, 4))
print(nested[2][1])
# Output: 4


# ---------------------------------------------------------


# 3️⃣ Set Practice (10 programs)
# 1. Create a set
s = {1, 2, 3, 4, 5}
print(s)
# Output: {1, 2, 3, 4, 5}

# 2. Add element
s.add(6)
print(s)
# Output: {1, 2, 3, 4, 5, 6}

# 3. Remove element
s.remove(3)
print(s)
# Output: {1, 2, 4, 5, 6}

# 4. Discard element (no error if not present)
s.discard(10)
print(s)
# Output: {1, 2, 4, 5, 6}

# 5. Union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
# Output: {1, 2, 3, 4, 5}

# 6. Intersection
print(s1.intersection(s2))
# Output: {3}

# 7. Difference
print(s1.difference(s2))
# Output: {1, 2}

# 8. Symmetric difference
print(s1.symmetric_difference(s2))
# Output: {1, 2, 4, 5}

# 9. Check subset
print({1, 2}.issubset(s1))
# Output: True

# 10. Clear set
s.clear()
print(s)
# Output: set()


#-------------------------------------------------------------------------------------- 



# 4️⃣ Dictionary Practice (10 programs)
# 1. Create a dictionary
student = {"name": "Krishna", "age": 21, "city": "Meerut"}
print(student)

# 2. Access value by key
print(student["name"])

# 3. Add new key-value
student["course"] = "Python"
print(student)

# 4. Update value
student["age"] = 22
print(student)

# 5. Delete key
del student["city"]
print(student)

# 6. Get value safely
print(student.get("city", "Not Found"))

# 7. Keys and values
print(student.keys(), student.values())

# 8. Items
print(student.items())

# 9. Loop through dictionary
for k, v in student.items():
    print(k, ":", v)

# 10. Nested dictionary
students = {
    "s1": {"name": "Amit", "age": 20},
    "s2": {"name": "Neha", "age": 21}
}
print(students["s2"]["name"])

# ---------------------------------------------------------------------------------------------------------------

1️⃣ List Practice (10 programs)
# 1. Create a list and print it
numbers = [10, 20, 30, 40, 50]
print(numbers)
# Output: [10, 20, 30, 40, 50]

# 2. Access elements by index
print(numbers[0], numbers[-1])
# Output: 10 50

# 3. Add elements to a list
numbers.append(60)
print(numbers)
# Output: [10, 20, 30, 40, 50, 60]

# 4. Insert element at a position
numbers.insert(2, 25)
print(numbers)
# Output: [10, 20, 25, 30, 40, 50, 60]

# 5. Remove an element
numbers.remove(40)
print(numbers)
# Output: [10, 20, 25, 30, 50, 60]

# 6. Pop last element
last = numbers.pop()
print("Popped:", last, numbers)
# Output: Popped: 60 [10, 20, 25, 30, 50]

# 7. Slice list
print(numbers[1:4])
# Output: [20, 25, 30]

# 8. Reverse list
numbers.reverse()
print(numbers)
# Output: [50, 30, 25, 20, 10]

# 9. Sort list
numbers.sort()
print(numbers)
# Output: [10, 20, 25, 30, 50]

# 10. Sum and average
print("Sum:", sum(numbers), "Average:", sum(numbers)/len(numbers))
# Output: Sum: 135 Average: 27.0


# -------------------------------------------------------------------------------------------
# 2️⃣ Tuple Practice (10 programs)
# 1. Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
# Output: ('apple', 'banana', 'cherry')

# 2. Access tuple elements
print(fruits[1], fruits[-1])
# Output: banana cherry

# 3. Tuple slicing
print(fruits[0:2])
# Output: ('apple', 'banana')

# 4. Tuple concatenation
t2 = ("orange", "kiwi")
t3 = fruits + t2
print(t3)
# Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi')

# 5. Tuple repetition
print(fruits * 2)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 6. Check element existence
print("banana" in fruits)
# Output: True

# 7. Length of tuple
print(len(fruits))
# Output: 3

# 8. Count occurrences
t4 = (1,2,2,3,2)
print(t4.count(2))
# Output: 3

# 9. Index of element
print(fruits.index("cherry"))
# Output: 2

# 10. Nested tuple
nested = (1, 2, (3, 4))
print(nested[2][1])
# Output: 4
3️⃣ Set Practice (10 programs)
# 1. Create a set
s = {1, 2, 3, 4, 5}
print(s)
# Output: {1, 2, 3, 4, 5}

# 2. Add element
s.add(6)
print(s)
# Output: {1, 2, 3, 4, 5, 6}

# 3. Remove element
s.remove(3)
print(s)
# Output: {1, 2, 4, 5, 6}

# 4. Discard element (no error if not present)
s.discard(10)
print(s)
# Output: {1, 2, 4, 5, 6}

# 5. Union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
# Output: {1, 2, 3, 4, 5}

# 6. Intersection
print(s1.intersection(s2))
# Output: {3}

# 7. Difference
print(s1.difference(s2))
# Output: {1, 2}

# 8. Symmetric difference
print(s1.symmetric_difference(s2))
# Output: {1, 2, 4, 5}

# 9. Check subset
print({1, 2}.issubset(s1))
# Output: True

# 10. Clear set
s.clear()
print(s)
# Output: set()

# ---------------------------------------------------
# 4️⃣ Dictionary Practice (10 programs)

# 1. Create a dictionary
student = {"name": "Krishna", "age": 21, "city": "Meerut"}
print(student)
# Output: {'name': 'Krishna', 'age': 21, 'city': 'Meerut'}




# 2. Access value by key
print(student["name"])
# Output: Krishna




# 3. Add new key-value
student["course"] = "Python"
print(student)
# Output: {'name': 'Krishna', 'age': 21, 'city': 'Meerut', 'course': 'Python'}




# 4. Update value
student["age"] = 22
print(student)
# Output: {'name': 'Krishna', 'age': 22, 'city': 'Meerut', 'course': 'Python'}





# 5. Delete key
del student["city"]
print(student)
# Output: {'name': 'Krishna', 'age': 22, 'course': 'Python'}




# 6. Get value safely
print(student.get("city", "Not Found"))
# Output: Not Found





# 7. Keys and values
print(student.keys(), student.values())
# Output: dict_keys(['name', 'age', 'course']) dict_values(['Krishna', 22, 'Python'])



# 8. Items
print(student.items())
# Output: dict_items([('name', 'Krishna'), ('age', 22), ('course', 'Python')])



# 9. Loop through dictionary
for k, v in student.items():
    print(k, ":", v)
# Output:
# name : Krishna
# age : 22
# course : Python



# 10. Nested dictionary
students = {
    "s1": {"name": "Amit", "age": 20},
    "s2": {"name": "Neha", "age": 21}
}
print(students["s2"]["name"])
# Output: Neha