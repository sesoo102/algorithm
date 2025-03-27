# 게리맨더링

N = int(input())
population = [0] + list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]

for n in range(1,N+1):
    info = list(map(int, input().split()))


