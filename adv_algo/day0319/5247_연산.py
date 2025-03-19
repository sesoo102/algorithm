# 연산
from collections import deque

T = int(input())


def bfs(n, c):
    visited = set()  # 방문한 숫자를 저장할 집합
    q = deque()
    q.append([n, 0])
    visited.add(n)  # 시작 숫자 방문 표시

    while q:
        num, cnt = q.popleft()

        if num == M:
            return cnt

        if 1 <= num + 1 <= 1000000 and num + 1 not in visited:
            q.append([num + 1, cnt + 1])
            visited.add(num + 1)
        if 1 <= num - 1 <= 1000000 and num - 1 not in visited:
            q.append([num - 1, cnt + 1])
            visited.add(num - 1)
        if 1 <= num * 2 <= 1000000 and num * 2 not in visited:
            q.append([num * 2, cnt + 1])
            visited.add(num * 2)
        if 1 <= num - 10 <= 1000000 and num - 10 not in visited:
            q.append([num - 10, cnt + 1])
            visited.add(num - 10)


for test_case in range(1, T + 1):
    # 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만든다.
    N, M = list(map(int, input().split()))

    print(f"#{test_case} {bfs(N, 0)}")
