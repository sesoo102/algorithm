T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    total = 0
    for num in arr:
        total += num
    
    if total % len(arr) >= len(arr)/2:
        average = total//len(arr) + 1

    else: average = total//len(arr)

    print(f"#{test_case} {average}")