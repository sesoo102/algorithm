T = int(input())
for test_case in range(1, T+1):
    o, e = map(int, input().split())
    N = int(input())

    requests = []
    for _ in range(N):
        S, F = map(int, input().split())
        if 0 <= S and F <= e:
            requests.append((S, F))

    total = 0
    # 끝나는 시간이 빠른 순으로 정렬
    requests.sort(key=lambda x:x[1])

    last_end = o
    for start, end in requests:
        if start >= last_end:
            total += 1
            last_end = end
    
    print(f"{test_case} {total}")