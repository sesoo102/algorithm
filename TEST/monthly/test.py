T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[0]
    min_value = arr[0]
    for i in range(N):
        if max_value < arr[i]:
            max_value = arr[i]
    for j in range(N):
        if min_value > arr[j]:
            min_value = arr[j]
    
    ans = max_value - min_value
    print(f'#{test_case} {ans}')