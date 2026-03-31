import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

data = [30, 20, 50]
labels = ['A', 'B', 'C']

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.show()

