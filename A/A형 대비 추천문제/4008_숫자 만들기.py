# 숫자 만들기

"""
연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
1
5
2 1 0 1     각 연산자의 개수 +-*/
3 5 3 7 9   수식에 사용되는 숫자

1
5
2 1 0 1
3 5 3 7 9
"""

T = int(input())


def make_number(idx, total, plus, minus, multiply, divide):
    global max_value, min_value, number, N

    if idx == N:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    # 다음 숫자
    next_num = number[idx]

    if plus > 0:
        make_number(idx + 1, total + next_num, plus - 1, minus, multiply, divide)
    if minus > 0:
        make_number(idx + 1, total - next_num, plus, minus - 1, multiply, divide)
    if multiply > 0:
        make_number(idx + 1, total * next_num, plus, minus, multiply - 1, divide)
    if divide > 0:
        make_number(idx + 1, int(total / next_num), plus, minus, multiply, divide - 1)


for test_case in range(1, T + 1):
    N = int(input())
    plus, minus, multiply, divide = map(int, input().split())
    number = list(map(int, input().split()))

    max_value = -float("inf")
    min_value = float("inf")

    # 첫 번째 숫자로 시작
    make_number(1, number[0], plus, minus, multiply, divide)

    ans = abs(max_value - min_value)

    print(f"#{test_case} {ans}")
