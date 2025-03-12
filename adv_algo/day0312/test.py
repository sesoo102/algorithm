T = int(input())


def dfs(swap_count):
    global max_value

    # 현재 숫자로 변환
    current_value = int("".join(cards))

    # 최대값 갱신
    if current_value > max_value:
        max_value = current_value

    # 교환 횟수를 모두 사용했으면 종료
    if swap_count == N:
        return

    # 방문한 상태 저장 (중복 방지)
    state = (tuple(cards), swap_count)
    if state in visited:
        return
    visited.append(state)  # 🔥 set 대신 list 사용

    # 가능한 모든 위치에서 두 개의 숫자를 교환
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            # 숫자 스왑
            cards[i], cards[j] = cards[j], cards[i]

            dfs(swap_count + 1)  # 다음 교환 진행

            # 백트래킹: 원래 상태로 복구
            cards[i], cards[j] = cards[j], cards[i]


for test_case in range(1, T + 1):
    cards, str_N = input().split()
    cards = list(cards)
    N = int(str_N)  # 교환 횟수

    max_value = float("-inf")
    visited = []  # 🔥 set -> list로 변경

    dfs(0)

    # 🔥 DFS 종료 후 남은 교환 횟수가 홀수면 마지막 두 자리 변경
    if (N - (len(visited) % N)) % 2 == 1:
        cards = list(str(max_value))
        cards[-1], cards[-2] = cards[-2], cards[-1]
        max_value = int("".join(cards))

    print(f"#{test_case} {max_value}")
