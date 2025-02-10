T = int(input())
# P: 전체 쪽 수, Pa: A가 찾을 쪽 번호, Pb: B가 찾을 쪽 번호


def binary_search(n, key):
    start = 1
    end = n
    count_num = 0
    while start <= end:
        middle = (start + end) // 2
        count_num += 1
        if middle == key:
            return count_num
        elif middle > key:
            end = middle
        else:
            start = middle
    return count_num


for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A_steps = binary_search(P, Pa)
    B_steps = binary_search(P, Pb)

    if A_steps < B_steps:
        print(f"#{test_case} A")

    elif A_steps > B_steps:
        print(f"#{test_case} B")

    else: print(f"#{test_case} 0")