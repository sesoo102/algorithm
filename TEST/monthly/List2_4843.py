# 특별한 정렬

T = int(input())

def special_sort(arr, N):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[idx]<arr[j]:
                    idx = j
        
        else:
            for j in range(i+1, N):
                if arr[idx] > arr[j]:
                    idx = j
        
        arr[i], arr[idx] = arr[idx], arr[i]
    

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    special_sort(numbers, N)

    result = numbers[:10]

    print(f"#{test_case}" + ' '.join(map(str, result)))