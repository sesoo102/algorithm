# 구간합

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    max_ans = -999999999
    min_ans = 999999999

    for i in range(N-M+1):
        c_sum = 0
        for j in range(M):
            c_sum += arr[i+j]

        if max_ans < c_sum:
            max_ans = c_sum

        if min_ans > c_sum:
            min_ans = c_sum
    
    ans = max_ans-min_ans

    print(f'#{test_case} {ans}')
