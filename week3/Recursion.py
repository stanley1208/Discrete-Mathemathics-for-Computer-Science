def factorial(n):
    assert(n>0)
    result=1
    for i in range(1,n+1):
        result*=i
    return result


print(factorial(10))


def factorial2(n):
    assert(n>0)

    if n==1:
        return 1
    else:
        return n*factorial2(n-1)

print(factorial2(10))


def infinite(n):
    if n==1:
        return 0
    return n*infinite(n+1)

# print(infinite(2))

def factorial3(n):
    return n*factorial3(n-1)

# print(factorial3(5))

def infinite2(n):
    if n==1:
        return 0
    return 1+infinite2(n)

print(infinite2(2))