friends = ["A", "B", "C", "D", "E"]
N = 5
# 최소 2 병 이상의 친구를 선정


# 1 인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for _ in range(N):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


answer = 0


def get_sub(n):
    for i in range(N):
        if n & 0x1:
            print(len(friends) - 6)
            # 필요한 연산.
        n >>= 1


# 모든 부분 집합을 확인
for target in range(1 << N):
    # 만약, 원소의 개수가 2개 이상이라면 answer += 1
    if get_count(target) >= 2:
        answer += 1

print(answer)
