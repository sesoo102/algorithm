# 부분 수열의 합합

T = int(input())


# 백트래킹으로 부분 수열의 합 찾기
def subset(idx, total):
    global count

    # 모든 원소를 탐색했으면 종료
    if idx == N:
        if total == K:  # 합이 K인 경우
            count += 1
        return

    # 현재 원소를 포함하는 경우
    subset(idx + 1, total + A[idx])

    # 현재 원소를 포함하지 않는 경우
    subset(idx + 1, total)


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0  # 정답 개수 저장
    subset(0, 0)  # 백트래킹 시작

    print(f"#{test_case} {count}")
