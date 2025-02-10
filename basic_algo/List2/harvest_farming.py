T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [[int(num) for num in input()] for _ in range(N)]
    '''
    for _ in range(N):
        [int(num) for num in input()]
    '''
    # arr = [list(map(int, list(input().strip()))) for _ in range(N)]
    total_harvest = 0
    mid = N // 2

    for r in range(N):
        if r <= mid:
            start = mid -r
            end = mid +r
            for c in range(start, end + 1):
                total_harvest += arr[r][c]

        else:
            start = mid -(N - 1 - r)
            end = mid +(N -1 + r)
            for c in range(start, end + 1):
                total_harvest += arr[r][c]

    print(f'#{test_case} {total_harvest}')