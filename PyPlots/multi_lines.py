import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 5., 0.1)
y1 = 2 + 1.0*x
y2 = 2 + 2.0*x
y3 = 2 + 3.0*x

plt.plot(x, y1, x, y2, x, y3)
plt.show()
