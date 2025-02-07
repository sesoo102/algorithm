N = input()
N = int(N)
my_list = []

for n in range(1,1001):
    if n <= N:
        if N % n == 0:
            my_list.append(n)
    else:
        break

print(" ".join(map(str, my_list)))