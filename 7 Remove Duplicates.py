lst = [1,2,2,3]
res = []
for i in lst:
    if i not in res:
        res.append(i)
print(res)

#input: [1,2,2,3]
#output: [1, 2, 3]
