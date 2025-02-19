'''
4
70 42 47 32
11 97 37 59
75 90 5 81
84 42 11 59
'''

# 4방 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# (r, c)와 주변 4칸 중에서 (r,c)에 있는 값이 최소값인지
def is_min(r, c):
    # 나 (r, c) 하고 주변 4개랑 비교하면 내가 최소인지 알 수 있다.
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] < arr[r][c]: # 나보다 작은 값이 있다면
                return False # 내가 최소값이 아님
    return True #내가 최소값


def find_min_neighbor(r, c):
    min_val = arr[r][c] # 가운데 값이 최소값이라고 일단 가정.
    min_r, min_c = r, c # r, c 가 최소값의 좌표라고 일단 가정.
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N: # 경계조건은 반드시 체크크
            if arr[nr][nc] < min_val: # 최소값보다 작은 값을 찾으면.
                min_val = arr[nr][nc] # 그걸로 업데이트
                min_r, min_c = nr, nc
    return min_r, min_c


def simulation(r, c):
    # 내가 최소값이 될 때까지 반복해야 함
    # 내가 최소값이 아니라면, 반복해서 탐색해야 함
    cnt = 1
    while not is_min(r, c):
        # 4개 중 가장 작은 거 찾아서
        nr, nc = find_min_neighbor(r, c) # (r,c)기준 최소값 이웃의 좌표를 찾아 반환하는 함수
        # 거기로 가기
        r, c  = nr, nc
        cnt += 1
    
    return cnt


# 완전탐색 : 모든 점을 출발점으로 하여 시뮬레이션을 해야 함
N = int(input()) # 배열의 크기
arr = [list(map(int, input().split())) for _ in range(N)]

# (0,0) ~ (3,3)까지 모든 점을 대상으로 해서 시뮬레이션
max_cnt = 0
for r in range(N):
    for c in range(N):
        # (r, c) : 출발점 
        cnt = simulation(r, c)
        max_cnt = max(max_cnt, cnt)
print(max_cnt)
