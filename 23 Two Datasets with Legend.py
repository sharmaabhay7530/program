import matplotlib.pyplot as plt # pyright: ignore[reportMissingModuleSource]

x = [1, 2, 3]
y1 = [2, 4, 6]
y2 = [1, 3, 5]

plt.plot(x, y1, label='Data1')
plt.plot(x, y2, label='Data2')
plt.legend()
plt.show() 

