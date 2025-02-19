import random

N = 6
arr = [[str(random.randint(1, 15)) for c in range(N)] for r in range(N)]
print(arr)

print(N)
for row in arr:
    print(' '.join(row))
