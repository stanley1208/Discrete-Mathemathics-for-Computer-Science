import numpy as np
import matplotlib.pyplot as plt

for m in [10,15]:
    plt.clf()
    n=np.linspace(2,m)
    plt.plot(n,n**3,label="$n^3$")
    plt.plot(n, 2**n, label="$2^n$")
    plt.legend(loc='best')

    plt.show()
