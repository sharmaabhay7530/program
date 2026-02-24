
d = {"name": "Krishna", "age": 22, "city": "Delhi"}

# 1. clear()
# Removes all items.
d.clear()
print(d)
# Output:
# {}



# 2. copy()
# Creates a shallow copy.
d = {"a": 1, "b": 2}
d2 = d.copy()
print(d2)
#Output:
# {'a': 1, 'b': 2}




# 3. fromkeys()
# Creates dictionary from keys.
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)
#Output:
#{'a': 0, 'b': 0, 'c': 0}





#  4. get()
# Returns value of key.
d = {"a": 10}
print(d.get("a"))
print(d.get("b", "Not Found"))
# Output:
# 10
# Not Found
# (No error if key missing 🔥)



# 5. items()
# Returns key-value pairs.
d = {"a": 1, "b": 2}
print(d.items())
# Output:
# dict_items([('a', 1), ('b', 2)])




#  6. keys()
#Returns all keys.
print(d.keys())
# Output:
# dict_keys(['a', 'b'])




#7. values()
# Returns all values.
print(d.values())
# Output:
# dict_values([1, 2])





# 8. pop()
# Removes specific key.
d = {"a": 1, "b": 2}
d.pop("a")
print(d)
# Output:
# {'b': 2}



# 9. popitem()
# Removes last inserted item (Python 3.7+).
d = {"a": 1, "b": 2}
d.popitem()
print(d)
# Output:
# {'a': 1}
# (Removes 'b')




# 10. setdefault()
# Returns value if key exists, otherwise inserts key.
d = {"a": 1}
d.setdefault("b", 100)
print(d)
# Output:
# {'a': 1, 'b': 100}





# 11. update()
# Updates dictionary with new values.
d = {"a": 1}
d.update({"b": 2})
print(d)
# Output:
# {'a': 1, 'b': 2}