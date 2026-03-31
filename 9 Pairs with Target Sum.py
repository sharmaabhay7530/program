lst = [2,4,3,5]
target = 7
print([(i,j) for i in lst for j in lst if i+j==target and i<j])

#input: lst = [2,4,3,5], target = 7
#output: [(2, 5), (4, 3)]
