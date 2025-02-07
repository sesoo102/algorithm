T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # max 값 찾기
    max_value = arr[0]
    for i in range(N):
        if arr[i] > max_value:
            max_value = arr[i]

    # min 값 찾기
    min_value = arr[0]
    for i in range(N):
        if arr[i] < min_value:
            min_value = arr[i]

    # 차이 출력
    answer = max_value - min_value

    print(f"#{test_case} {answer}")