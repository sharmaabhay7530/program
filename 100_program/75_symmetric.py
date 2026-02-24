# Problem 75: Find symmetric difference of two sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())

sym_diff_set = set1 ^ set2  # symmetric difference
print("Symmetric difference of sets:", sym_diff_set)


'''output
Enter elements of first set separated by space: 6  6 476  3 64 3 5 
Enter elements of second set separated by space:  63 53 53 636 235 
Symmetric difference of sets: {'235', '3', '6', '476', '636', '63', '64', '53', '5'}'''