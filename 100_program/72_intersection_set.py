# Problem 72: Perform intersection of two sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())

intersection_set = set1 & set2  # intersection
print("Intersection of sets:", intersection_set)

'''output
Enter elements of first set separated by space: 2 5 3 7 3 7 3
Enter elements of second set separated by space:  24 3 6 3 6 3 
Intersection of sets: {'3'}'''