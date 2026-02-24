# Problem 73: Perform difference of two sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())

difference_set = set1 - set2  # elements in set1 not in set2
print("Difference of sets (set1 - set2):", difference_set)

'''output
Enter elements of first set separated by space: 42 44 66 44 7 6
Enter elements of second set separated by space: 6 3 6 5 8 4 6
Difference of sets (set1 - set2): {'44', '66', '7', '42'}'''