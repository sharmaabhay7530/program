n = 153
print(n == sum(int(i)**len(str(n)) for i in str(n)))

#input: 153
#output: True
