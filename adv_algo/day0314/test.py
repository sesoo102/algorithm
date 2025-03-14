def comb(idx, start_i):
    if idx == R:
        for i in range(N):
            if selected[i]:
                print(arr[i], end=" ")
        print()
        return

    for i in range(start_i, N):
        if not selected[i]:
            selected[i] = True
            comb(idx + 1, i + 1)
            selected[i] = False


arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
selected = [False] * N


comb(0, 0)
