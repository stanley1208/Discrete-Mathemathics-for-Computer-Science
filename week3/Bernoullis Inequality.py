import matplotlib.pyplot as plt
import numpy as np


sample=200
# compound interest
x=np.arange(sample)
y=1.02**x
plt.plot(x,y)
plt.xlabel('n')
plt.ylabel('Money')
# simple interest
z=1+0.02*x
plt.plot(x,z)

plt.show()