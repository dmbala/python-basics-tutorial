import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 10, 100)
y = x**2.0
plt.subplot(1,2,1)
plt.scatter(x,y)
plt.subplot(1,2,2)
plt.hist(x)
plt.show()
