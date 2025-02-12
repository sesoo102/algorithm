T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N = int(input()) # 버스 노선의 수
    bus_lines = [] # 버스 노선을 저장할 리스트
    # 각 노선은 튜플로 저장(A, B)
    for _ in range(N):
        A, B = list(map(int, input().split()))
        bus_lines.append((A, B))
    
    P = int(input()) # 정류장의 수
    stations = [] # 정류장 번호를 저장할 배열
    for _ in range(P): # P개의 정류장 번호를 저장
        station = int(input())
        stations.append(station)
    cnt = [0] * P # 카운팅 배열
    # [1, 2, 3, 4, 5]
    # stations = [999, 21, 5, 20, 200]
    # cnt      = [ 2,   0 ,1, 2,   1]

    for j in range(P): # j인덱스에 위치한 정류장 번호를
        for i in range(N): # 모든 버스 노선에 대해 검사
            A, B = bus_lines[i]
            if A <= stations[j] <= B:
                cnt[j] += 1

    # 숫자를 조인할 수 없으므로, 문자열로 변환한 후 조인.
    cnt = [str(n) for n in cnt]
    print(f"#{tc} {' '.join(cnt)}")

