# 전기버스2

T = int(input())


def bus(idx, cnt):
    global min_value

    # 최소값보다 크면 가지치기
    if cnt >= min_value:
        return

    # 종점 도착
    if idx >= N - 1:
        if min_value > cnt:
            min_value = cnt
        return

    # 가능한 모든 경우 탐색
    for i in range(1, stops[idx] + 1):
        bus(idx + i, cnt + 1)


for test_case in range(1, T + 1):
    N, *stops = list(map(int, input().split()))

    min_value = 999999999

    # 출발지에서의 배터리 장착은 횟수에서 제외
    bus(0, -1)

    print(f"#{test_case} {min_value}")
