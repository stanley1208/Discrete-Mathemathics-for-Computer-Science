import itertools as it


def is_solution(perm):
    for (i1,i2) in it.permutations(range(len(perm)),2):
        if abs(i1-i2) ==abs(perm[i1]-perm[i2]):
            return False

    return True

assert (is_solution([1,3,0,2])==True)
assert (is_solution([3,1,0,2])==False)

# for perm in it.permutations(range(8)):
#     if is_solution(perm):
#         print(perm)
#         exit()