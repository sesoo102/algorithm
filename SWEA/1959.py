T = int(input())
for test_case in range(1, T + 1):
    # N개의 숫자로 구성된 숫자열 Ai
    # M개의 숫자로 구성된 숫자열 Bj
    N, M = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    # a가 더 길때
    if N > M:
        total_list = []
        for m in range(N-M+1):
            total = 0
            for n in range(M):
                try:
                    total += Ai[n+m]*Bj[n]
                except IndexError:
                    break
            total_list.append(total)
            
    else:
        total_list = []
        for m in range(M-N+1):
            total = 0
            for n in range(N):
                try:
                    total += Ai[n]*Bj[n+m]
                except IndexError:
                    break
            total_list.append(total)

    max_val = -999999999
    for num in total_list:
        if num > max_val:
            max_val = num

    print(f'#{test_case} {max_val}')




# 최적화 코드
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 긴 배열을 long_arr, 짧은 배열을 short_arr로 설정
    if N > M:
        long_arr, short_arr = Ai, Bj
        L, S = N, M
    else:
        long_arr, short_arr = Bj, Ai
        L, S = M, N

    max_val = -999999999  # 최대값 초기화

    # 슬라이딩 윈도우 방식으로 곱의 합 계산
    for m in range(L - S + 1):
        total = 0
        for n in range(S):
            total += long_arr[n + m] * short_arr[n]  # IndexError가 발생할 가능성이 없으므로 try-except 제거
        if total > max_val:  # 최대값 갱신
            max_val = total

    print(f'#{test_case} {max_val}')
