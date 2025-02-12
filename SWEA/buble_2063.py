N = int(input())
arr = list(map(int, input().split()))

# 버블 정렬 함수
def bubble_sort(arr):
    for i in range(len(arr) - 1):  # 전체 리스트 길이 - 1 만큼 반복
        for j in range(len(arr) - 1 - i):  # 정렬된 부분 제외하고 비교
            if arr[j] > arr[j + 1]:  # 앞에 있는 값이 더 크면 자리 바꿈
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

sorted_arr = bubble_sort(arr)  # 버블 정렬 수행
middle = N // 2  # 중앙값 인덱스 찾기

print(sorted_arr[middle])  # 중앙값 출력