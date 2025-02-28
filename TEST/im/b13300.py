# 방 배정
'''
한 방에는 같은 성별, 같은 학년.
'''
# N 수학여행에 참가하는 학생 수, K 한 방에 배정할 수 있는 최대 인원 수
N, K = list(map(int, input().split()))

w_cnt = [0] * 7
m_cnt = [0] * 7
ans = 0

for n in range(N):
    # S 성별, Y 학년
    # 0 여학생, 1 남학생. 1 <= Y <= 6
    S, Y = list(map(int, input().split()))
    
    if S == 0:
        w_cnt[Y] += 1
    
    elif S == 1:
        m_cnt[Y] += 1

for i in range(7):
    if w_cnt[i] != 0:
        ans += (w_cnt[i]//K + 1)
    if m_cnt[i] != 0:
        ans += (m_cnt[i]//K + 1)

print(ans)
    

