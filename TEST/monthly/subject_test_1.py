T = int(input())

for team in range(1, T+1):
    N, M = list(map(int, input().split()))
    # N명의 사람들의 깃발 초기 상태, 문제의 번호와 인덱스 번호를 맞추기 위해 맨 앞에 [0] 추가
    arr = [0] + list(map(int, input().split()))
    # M줄에 걸친 a, b, c 명령 상태. a: 난이도, b: 기준번호, c: 사람수
    for _ in range(M):
        a, b, c = list(map(int, input().split()))

        # b번 부터 c명의 사람들의 깃발 상태 변화.
        for i in range(c):
            if b+c-1 <= N:
                arr[b+i] = (arr[b+i]+1) % 2

    print(f'#{team} {" ".join(map(str, arr[1:]))}')