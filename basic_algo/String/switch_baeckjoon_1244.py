N = int(input())
# 문제의 주어진 번호를 그대로 쓰기 위해서 길이가 N+1인 배열을 만듬.
switch = [0] + list(map(int, input().split()))
student_number = int(input())
for i in range(student_number):
    gender, num = list(map(int, input().split()))

    if gender == 1:  # 남학생이라면
        for i in range(num, N+1, num):
            switch[i] = (switch[i] + 1) % 2
    elif gender == 2:
        # 자기자신의 스위치를 일단 켜고 끈다.
        switch[num] = (switch[num]+1) %2
        # 그 다음 양 옆을 보기
        j = 1
        while num - j >= 1 and num + j <= N and switch[num-j] == switch[num+j]:
            switch[num-j] = (switch[num-j]+1)%2
            switch[num+j] = (switch[num+j]+1)%2
            j +=1

for i in range(1, N+1, 20):
    print(' '.join([str(n) for n in switch[i: i+20]]))