T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    time = 1
    visited = [0] * 401  # 방 번호를 그대로 사용

    # 이동 경로 입력
    for _ in range(N):
        S, E = map(int, input().split())

        # S가 항상 작은 값이 되도록 정렬
        if S > E:
            temp = S
            S = E
            E = temp

        # 짝수 방이면 같은 복도로 묶이도록 S-1 처리
        if S % 2 == 0:
            S -= 1
        if E % 2 == 1:
            E += 1  # 짝수 방이면 한 칸 줄여서 같은 복도로 인식

        # 이동하는 방 범위 증가
        for i in range(S, E + 1):
            visited[i] += 1
            if visited[i] > time:
                time = visited[i]

    print(f"#{test_case} {time}")
