# view

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    total_view =0

    for i in range(2, N-2):
        max_view = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

        if arr[i] > max_view:
            total_view += arr[i] - max_view


    print(f"#{test_case} {total_view}")