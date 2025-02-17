# 벌집
n = int(input())

# # 6의 배수 더하기 재귀함수
# # 재귀가 너무 깊어져서 런타임 에러 발생.
# def six(ans):
#     if ans == 0:
#         return 1
#
#     else:
#         return six(ans-1) + 6*ans
# a = 0
# while n > six(a):
#     a += 1
#
# print(a+1)

n = int(input())

ans = 1  # 시작 값 (six(0) = 1)
a = 0

while n > ans:
    a += 1
    ans += 6 * a

print(a + 1)

