import numpy as np # pyright: ignore[reportMissingImports]
import matplotlib.pyplot as plt # type: ignore

data = np.random.randn(100)

plt.hist(data)
plt.show() 

