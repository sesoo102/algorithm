for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        # arr 에서 최댓값 찾기
        max_index = arr[0]
        for i in range(len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i

        # arr 에서 최솟값 찾기
        min_index = arr[0]
        for i in range(len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        # dump 과정
        arr[max_index] -= 1
        arr[min_index] += 1

        if arr[max_index] - arr[min_index] <= 1:
            break

    answer = max(arr) - min(arr)

    print(f"#{test_case} {answer}")