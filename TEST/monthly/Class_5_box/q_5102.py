# 노드의 거리

"""
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.

E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

"""

from collections import deque

def bfs(start):
    global G, V, adj
    visited = [0] * (V+1)

    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        tnode = q.popleft()
        if tnode == G:
            return visited[tnode] -1
        else:
            for i in range(1, V+1):
                if visited[i] == 0 and adj[tnode][i] == 1:
                    q.append(i)
                    visited[i] = visited[tnode] + 1
    return 0



T = int(input())

for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))

    adj = [[0] * (V + 1) for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj[v1][v2] = 1
        adj[v2][v1] = 1
    S, G = list(map(int, input().split()))
    
    ans = bfs(S)

    print(f"#{test_case} {ans}")
    
