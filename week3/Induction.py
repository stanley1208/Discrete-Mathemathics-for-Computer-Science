def sum_of_integers(n):
    assert n > 0
    return sum(range(1, n + 1))

print(all(sum(range(1, n + 1)) == n * (n + 1) // 2
          for n in range(1, 101)))