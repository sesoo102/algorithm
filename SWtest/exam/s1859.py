# 백만 장자 프로젝트
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for n in range(N):
        max_value = 0
        for i in range(n+1, N):
            if max_value < arr[i]:
                max_value = arr[i]

        if arr[n] < max_value:
            ans += (max_value - arr[n])
    
    print(f'#{test_case} {ans}')

# 시간초과 발생 -> 배열을 끝에서부터 역순으로 탐색
# 얘는는 런타임 에러가 나오네 ㅋㅋ
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = 0  # 현재까지의 최대값 (뒤에서부터 갱신)
    ans = 0

    # 배열을 뒤에서부터 탐색
    for i in range(N-1, -1, -1):
        if arr[i] > max_value:
            max_value = arr[i]  # 새로운 최대값 갱신
        else:
            ans += (max_value - arr[i])  # 차익 계산

    print(f'#{test_case} {ans}')