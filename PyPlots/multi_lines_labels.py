import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., 5., 0.1)
y1 = 2 + 1.0*x
y2 = 2 + 2.0*x
y3 = 2 + 3.0*x


plt.plot(x, y1, marker="o") 
plt.plot(x, y2, marker="*") 
plt.plot(x, y3, marker="+") 
plt.title("Python experience with time")
plt.xlabel("time")
plt.ylabel("Productivity")
plt.show()
