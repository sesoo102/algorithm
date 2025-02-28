# 삼성시의 버스 노선

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stops = [0]*5001

    for _ in range(N):
        A, B = list(map(int, input().split()))

        for i in range(A, B+1):
            stops[i] += 1
    
    P = int(input())
    P_stops = [int(input()) for _ in range(P)]

    result =[]

    for P_stop in P_stops:
        result.append(str(stops[P_stop]))
 
    print(f'#{test_case} {" ".join(result)}')
