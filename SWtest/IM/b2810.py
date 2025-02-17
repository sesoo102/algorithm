# 컵홀더

N = int(input())
arr = list(map(str, input()))

count_L = 0
for n in range(N):
    if arr[n] == 'L':
        count_L += 1

couple = count_L // 2

if couple <= 1:
    print(N)

else:
    print(N + 1 -couple)