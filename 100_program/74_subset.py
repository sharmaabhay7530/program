# Problem 74: Check whether one set is subset of another\
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())

if set1 <= set2:
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")


'''output
Enter elements of first set separated by space: 2 5 3 7 4 7 4
Enter elements of second set separated by space: 2 45 3 5 3 5
First set is not a subset of second set.'''