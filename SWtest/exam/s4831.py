T = int(input())



for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    # 현재 위치
    i = 0
    # 충전 횟수
    cnt = 0
    # 현재 충전소 리스트의 인덱스
    charger_idx = 0

    while i < N:
        if i + K < N:
            break

        # 이동 가능한 범위 내 마지막 충전소 저장 변수
        last_charger = -1
        while charger_idx<M and charger[charger_idx]<=i+K:
            # 범위 내의 충전소 갱신
            last_charger=charger[charger_idx]
            # 충전소 인덱스 증가
            charger_idx += 1
        
        # 이동 범위 내 충전소가 없는 경우
        if last_charger == -1:
            cnt = 0
            break

        i = last_charger
        cnt += 1


    
