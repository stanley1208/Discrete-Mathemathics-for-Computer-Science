import matplotlib.pyplot as plt
import numpy as np


plt.xlabel("$n$")
plt.ylabel("Money ($)")


x=np.arange(200)
plt.plot(x,1.02**x,label='$1.02^n$')
plt.plot(x,1+0.02*x,label='$1+0.02*n$')
plt.legend(loc='best')
# plt.show()


def day_to_target(starting_amount,earn_percent,target_amount):
    day=1
    amount=starting_amount
    daily_factor=(1+earn_percent/100.0)
    while amount<target_amount:
        day+=1
        amount*=daily_factor
    return day

def print_example(starting_amount,earn_percent,target_amount):
    days=day_to_target(starting_amount,earn_percent,target_amount)
    print("starting_amount:",starting_amount)
    print("earn_percent:", earn_percent)
    print("days:",days)

print_example(1000,2,1000000)
print_example(1000,10,1000000)


def how_much_money(starting_amount,earn_percent,day):
    daily_factor = (1 + earn_percent / 100.0)
    return starting_amount*(daily_factor)**(day-1)

def print_example2(starting_amount,earn_percent,day):
    money=how_much_money(starting_amount,earn_percent,day)
    print("starting_amount:",starting_amount)
    print("earn_percent",earn_percent)
    print("days:",day)
    print("money:",money)

print_example2(1000,2,365)



