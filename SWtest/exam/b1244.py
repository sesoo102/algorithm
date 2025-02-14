# 스위치 켜고 끄기기

# 스위치 개수
N = int(input())
# 1 : ON, 0 : OFF
# 인덱스 번호와 스위치 번호를 맞추기 위해 arr[0]==0을 추가해줌.
arr = [0] + list(map(int, input().split()))

# 학생 수
student = int(input())

for i in range(student):
    gender, num = map(int, input().split())

    # 남자
    if gender == 1:
        for n in range(num, N+1, num):
            arr[n] = (arr[n]+1) % 2
                

    # 여자
    elif gender == 2:
        n = 1
        while num-n > 0 and num + n < N+1 and arr[num-n] == arr[num+n]:
            arr[num-n] = (arr[num-n]+1)%2
            arr[num+n] = (arr[num+n]+1)%2
            
            n += 1
            
        arr[num] = (arr[num]+1) % 2

for i in range(1, N+1, 20):
    print(' '.join([str(n) for n in arr[i: i+20]]))