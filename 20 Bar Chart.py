import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

products = ['A', 'B', 'C', 'D', 'E']
sales = [10, 20, 15, 25, 30]

plt.bar(products, sales)
plt.show()

