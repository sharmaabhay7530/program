s = "hello"
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
print(d)

#input: "hello"
#output: {'h': 1, 'e': 1, 'l': 2, 'o': 1} 