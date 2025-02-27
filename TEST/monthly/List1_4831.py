# 전기버스

T = int(input())

def charge(stops, n, k):
    my_stop = 0
    cnt = 0
    # my_stop == N 도착!
    while my_stop < n:
        candidates = [s for s in stops if s <= my_stop + k and s > my_stop]
        if my_stop + k >= n:
            return cnt
        
        if len(candidates) == 0:
            return 0
        else:
            my_stop = max(candidates)
            cnt +=1

for test_case in range(1, T + 1):
    # k: 한번 충전으로 최대 이동 정류장 수, N: 종점, M: 충전기 
    K, N, M = list(map(int, input().split()))
    charger_stops = list(map(int, input().split()))

    cnt = charge(charger_stops, N, K)

    print(f"#{test_case} {cnt}")

    
