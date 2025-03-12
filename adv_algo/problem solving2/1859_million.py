# 백만 장자 프로젝트

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 현재까지의 최대값 (뒤에서부터 갱신)
    max_value = 0
    ans = 0

    # 배열을 뒤에서부터 탐색
    for i in range(N - 1, -1, -1):
        if arr[i] > max_value:
            max_value = arr[i]
        else:
            ans += max_value - arr[i]

    print(f"#{test_case} {ans}")
