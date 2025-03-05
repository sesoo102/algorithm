'''
첫 줄에 총 정점 수 V.
V-1개의 간선 나열(부모 자식 순서로 표기)
간선은 부모 정점 번호가 작은 것부터 나열, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열
다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회, 방문한 정점(부모) 먼저 처리리
def pre_order(T):
    if T:   # 0이 아니면(존재하는 정점,자식이면)
        print(T, end = ' ')
        # 왼쪽 자식(서브트리)로 이동
        pre_order(left[T])
        # 오른쪽 자식(서브트리)로 이동
        pre_order(right[T])

N = int(input())        # 1번부터 N번까지인 정점
E = N-1                 # 간선 수
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장(N번까지 사용)
right = [0]*(N+1)       # 부로를 인덱스로 오른쪽 자식 저장

# root 찾기
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]

    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

'''
# 루트 찾기
root = 1
for i in range(1, N+1):
    if par[i] == 0:     # 부모 정점이 없으면 루트
        root = i
        break
'''



# N의 조상을 찾는 코드(루트도 찾을 수 있음)
c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)         # 루트 부터 전위 순회회