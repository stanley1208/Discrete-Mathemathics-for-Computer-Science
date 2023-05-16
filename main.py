import itertools as it


# def is_solution(perm):
#     for (i1,i2) in it.permutations(range(len(perm)),2):
#         if abs(i1-i2) ==abs(perm[i1]-perm[i2]):
#             return False
#
#     return True
#
# assert (is_solution([1,3,0,2])==True)
# assert (is_solution([3,1,0,2])==False)

# for perm in it.permutations(range(8)):
#     if is_solution(perm):
#         print(perm)
#         exit()

def extend(perm,n):
    if len(perm)==n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            print(perm)
            if can_be_extended_to_solution(perm):
                extend(perm,n)

            perm.pop()


def can_be_extended_to_solution(perm):
    i=len(perm)-1
    for j in range(i):
        if i-j==abs(perm[i]-perm[j]):
            return False

    return True


print(extend(perm=[],n=4))

