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
        exit()

