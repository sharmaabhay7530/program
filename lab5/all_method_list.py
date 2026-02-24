list1 = [1,2,3,4,5,6,7,8,9,10]

# append

list1.append(40)
print(list1)

#extend
list1.extend([3, 4])
print(list1)

#insert
list1.insert(1, 5)
print(list1)

#remove
list1.remove(2)
print(list1)

#pop
list1.pop()
print(list1)

#clear
list1.clear()

#index
print(list1.index(2))

#count
print(list1.count(1))

#sort
list1.sort()
print(list1)

#reverse
list1.reverse()

#copy
new_list = list1.copy()