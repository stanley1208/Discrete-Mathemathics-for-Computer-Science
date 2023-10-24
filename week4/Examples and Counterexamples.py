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

# for n in range(1,100):
#     if not is_prime(n**2+n+41):
#         print(n)
#         exit()


def is_prime2(n):
    return n!=1 and all(n%d!=0 for d in range(2,n))

print(next(n for n in range(1,100) if not is_prime2(n**2+n+41)))


for a,b,c in combinations(range(1,20),3):
    if a**2+b**2==c**2:
        print(f'{a}**2+{b}**2={c**2}')
