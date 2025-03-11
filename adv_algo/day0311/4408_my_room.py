T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    time = 1
    visited = [0] * 401

    for _ in range(N):
        S, E = map(int, input().split())

        if S > E:
            S, E = E, S

        # 홀짝 방번호
        if S % 2 == 0:
            S -= 1
        if E % 2 == 1:
            E += 1

        # 얼마나 겹쳤는지
        for i in range(S, E + 1):
            visited[i] += 1
            if visited[i] > time:
                time = visited[i]

    print(f"#{test_case} {time}")
