T = int(input())


def eating_candy(a, b):
    if a >= b:
        return a - b + 1
    return 0  # b > a일 경우 최소 0을 반환


for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())

    if B < 2 or C < 3:
        print(f"#{test_case} -1")
        continue

    ans = eating_candy(B, C) + eating_candy(A, C - 1)
    print(f"#{test_case} {ans}")
