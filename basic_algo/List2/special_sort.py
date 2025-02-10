T = int(input())

def special_sort(a,N):
    for i in range(10):
        idx = i
        # 최댓값
        if i % 2 == 0:
            for j in range(i+1, N):
                if a[idx] < a[j]:
                    idx = j
        # 최솟값
        else:
            for j in range(i+1, N):
                if a[idx] > a[j]:
                    idx = j
        a[i], a[idx] = a[idx], a[i]


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    special_sort(arr, N)

    print(f"#{tc} " + ' '.join(map(str, arr[:10])))