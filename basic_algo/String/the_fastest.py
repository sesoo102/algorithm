T = int(input())

def pattern_count(p, t):
    N = len(t)
    M = len(p)
    # i는 p의 idx
    i = 0
    cnt = 0
    while i <= N - M:
        if t[i:i+len(p)] == p:
            cnt += 1
            i += len(p)
        else:
            i += 1
    return cnt

for tc in range(1, T+1):
    A, B = list(map(str, input().split()))

    a = len(A)
    b = len(B)

    p_count = pattern_count(B, A)
    result = a - b*p_count + p_count

    print(f"#{tc} {result}")

