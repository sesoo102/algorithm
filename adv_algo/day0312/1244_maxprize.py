T = int(input())


def dfs(swap_count):
    global max_value
    if swap_count == N:  # 교환 횟수가 N에 도달하면 최대값 갱신
        max_value = max(max_value, int("".join(cards)))
        return

    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]

            new_value = int("".join(cards))

            if (swap_count, new_value) not in visited:  # 방문하지 않은 상태라면
                visited.append((swap_count, new_value))  # 방문 처리
                dfs(swap_count + 1)

            # 백트래킹: 원래 상태로 복구
            cards[i], cards[j] = cards[j], cards[i]


for test_case in range(1, T + 1):
    cards, str_N = input().split()  # 숫자판 정보, 교환 횟수 입력받기
    cards = list(cards)
    N = int(str_N)

    visited = []
    max_value = 0
    dfs(0)

    print(f"#{test_case} {max_value}")
