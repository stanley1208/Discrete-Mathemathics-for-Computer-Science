from itertools import accumulate
import matplotlib.pyplot as plt


n=1000
sums=[*accumulate(1/(i*(i+1)) for i in range(1,n+1))]

for k in (n//10,n):
    plt.clf()
    plt.plot(sums[:k])
    plt.savefig(f'sum{k}.png')
    plt.show()

