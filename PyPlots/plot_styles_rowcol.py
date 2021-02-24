import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 10, 100)
y = x**2.0
y1 = x**3.0
plt.subplot(2,2,1)
plt.scatter(x,y)
plt.subplot(2,2,2)
plt.hist(x)

plt.subplot(2,2,3)
plt.scatter(x,y1)
plt.subplot(2,2,4)
plt.hist(x)
plt.show()
