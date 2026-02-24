# Problem 71: Perform union of two sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())

union_set = set1 | set2  # union operation
print("Union of sets:", union_set)

'''output
Enter elements of first set separated by space: 3 5 7 4 2 5 8 3 2 
Enter elements of second set separated by space: 2 
Union of sets: {'5', '8', '2', '3', '4', '7'}
PS C:\anudeep.foundation> '''