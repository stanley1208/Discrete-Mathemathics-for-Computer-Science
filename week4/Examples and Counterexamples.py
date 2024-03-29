from itertools import combinations


for n in range(100):
    if int(str(2**n)[:2])==65:
        print(f'2**{n}={2**n}')


def is_prime(n):
    assert n>0
    if n==1:
        return False

    for d in range(2,n):
        if n%d==0:
            return False

    return True

for n in range(1,100):
    if not is_prime(n**2+n+41):
        print(n)
#         exit()


def is_prime2(n):
    return n!=1 and all(n%d!=0 for d in range(2,n))

print(next(n for n in range(1,100) if not is_prime2(n**2+n+41)))


for a,b,c in combinations(range(1,20),3):
    if a**2+b**2==c**2:
        print(f'{a}**2+{b}**2={c}**2')



for a,b,c in combinations(range(1,20),3):
    if a**3+b**3==c**3:
        print(f'{a}**3+{b}**3={c}**3')

print(95800 ** 4 + 217519 ** 4 + 414560 ** 4)
print(422481 ** 4)
print(27**5+84**5+110**5+133**5)
print(144**5)

x = -80538738812075974
y = 80435758145817515
z = 12602123297335631

print(x ** 3 + y ** 3 + z ** 3)