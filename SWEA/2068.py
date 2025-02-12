# T = int(input())
# num =[input().split() for _ in range(T)]

# for i in range(1, T+1):
#     my_list = num[i]

# my_list.sort
# print(my_list[-1])
    

# # num = [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]
# # num.sort()
# # print(num)
# # print(num[-1])

# T = int(input())
# num = [list(map(int, input().split())) for _ in range(T)]  # 문자열을 정수 리스트로 변환

# for row in num:
#     print(max(row))  # 각 행에서 최대값 출력




T = int(input())
num = []

for _ in range(T):
    num.extend(map(int, input().split())) 

num.sort()
print(num[-1]) 

