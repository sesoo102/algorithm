T = int(input())
A = list(i for i in range(1, 13))
subset_list = []

# A의 부분집합 리스트 만들기
for i in range(1 << 12):
    subset = []
    for j in range(12):
        if i & (1 << j):
            subset.append(A[j])
    subset_list.append(subset)


# 문제조건
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))

    s = 0

    # N
    for i in range(len(subset_list)):
        candidate = []
        if len(subset_list[i]) == N:
            candidate.append(subset_list[i])

            # K
            for j in range(len(candidate)):

                candidate_sum = 0
                for num in candidate[j]:
                    candidate_sum += num

                if candidate_sum == K:
                    s += 1

    print(f"#{test_case} {s}")