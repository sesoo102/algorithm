T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    odd_sum = 0
    for num in arr:
        if num % 2 == 1:
            odd_sum += num
            
    print(f"#{test_case} {odd_sum}")