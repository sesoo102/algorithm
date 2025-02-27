# min max

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    max_value = number[0]
    for i in range(N):
        if max_value < number[i]:
            max_value = number[i]
    
    min_value = number[0]
    for j in range(N):
        if min_value > number[j]:
            min_value = number[j]
    
    ans = max_value - min_value

    print(f"#{test_case} {ans}")