# Let's consider:
# 1 = /
# 2 = \
# 0 = Empty

def can_be_extended(perm):
    i = len(perm) - 1 # Last cell index of the partial perm
    j = perm[i] # Value of the last cell of the partial perm
    j_op = 2 if j == 1 else 1 # Opposite value of the last cell of the partial perm
    if i == 25:
        return False # If the last cell is the 25th then we can't continue
    if j == 0: # If j = 0 then we know that we can continue
        return True
    # Here we check the constraints of the diagonals
    # I'm only using a one dimensional array so I use subtraction and remainder
    # (and a few restrictions to avoid weird indexes) to get the neighbors cells
    if (i >= 5 and perm[i - 5] == j_op) or (i >= 1 and perm[i - 1] == j_op):
        return False
    if j == 1 and i >= 4 and i % 5 != 4 and perm[i - 4] == 1:
        return False
    if j == 2 and i >= 6 and i % 5 != 0 and perm[i - 6] == 2:
        return False
    # If everything is ok then we can continue :)
    return True


def extend(per, diag, n):
    if diag == n: # Here i check if i already found the n solutions
        print(per)
        exit()
    # This is optimization, if i can't complete the 16 diagonals with the remaining cells,
    # then there is no point in continuing
    if 25 - len(per) + diag < n:
        return
    #  I suppose that this can be constant in the outer scope, but idk, here it is
    options = [2, 1, 0]
    for j in options:
        per.append(j)
        if j > 0:
            diag += 1 # Add 1 if append a diagonal (1 or 2)
        if can_be_extended(per):
            extend(per, diag, n)
        per.pop()
        if j > 0:
            diag -= 1
    return


if __name__ == '__main__':
    extend([], 0, 16)
