# 색종이

# N 색종이 장수
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]


for n in range(1, N+1):
    i, j, W, H = list(map(int, input().split()))

    for w in range(W):
        for h in range(H):
            arr[i+w][j+h] = n


for n in range(1, N+1):
    cnt = 0    
    for p in range(1001):
        for q in range(1001):
            if arr[p][q] == n:
                cnt += 1
    print(cnt)
