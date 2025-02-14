# 카드2 pop 때문에 시간초과과
n = int(input())

arr = [i for i in range(n, 0, -1)]

while len(arr) != 1:
    arr.pop()
    arr = [arr[-1]] + arr
    arr.pop()
print(arr[0])