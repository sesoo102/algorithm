T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    cnt = [0] * 1001
    for i in arr:
        cnt[i] += 1
    
    ans = 0
    for j in range(1, 1001-K):
        for k in range(K):
            ans += cnt[j+k]

    max_value = -1
    if max_value < ans:
        max_value = ans
    
    print(max_value)