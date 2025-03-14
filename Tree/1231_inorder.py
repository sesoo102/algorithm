# 중위순회
'''
중위 순회
def in_order
    if
        left
        루트 방문 할일
        right

완전이진트리

10개의 테스트 케이스(입력x)

N: 트리가 갖는 정점의 총 수
for _ range(N):
    정점 정보
'''
def in_order(n):
    global word     # 전역 변수 선언
    if n<= N:       # 방문하는 노드번호 n이 범위(N)안에 있다면
        # 중위순회
        in_order(n*2)       # 왼쪽 자식 노드
        word += tree[n]
        in_order(n*2+1)     # 오른쪽 자식 노드
 
for test_case in range(1, 11):
    # N 노드 개수
    N = int(input())
    
    # 완전 이진 트리(해당 노드에 문자)
    tree = [""] *(N+1)


    for i in range(N):
        # 노드번호, 문자, 자식(left, right)
        idx, alphabet, *c = list(input().split())       # () 형태로 자식노드를 받는다.
        idx = int(idx)
        tree[idx] = alphabet
         
         
    word = ''   # 중위 순회를 통해 문자열 만들기위해 초기화
    in_order(1)     # 루트 노드(1번 노드)에서 중위순회 시작
    print(f'#{test_case} {word}')









# def in_order(n):
#     global word
#     if n <= N:
#         # 왼쪽 자식
#         in_order(n*2)
#         # 알파벳
#         word += arr[n-1][1]
#         # 오른쪽 자식
#         in_order(n*2+1)

# for tc in range(1,11):
#     # 트리가 갖는 정점의 총 수
#     N = int(input())
#     # 정점 번호, 해당 정점 알파벳, 왼쪽 자식, 오른쪽 자식
#     arr = [input().split() for _ in range(N)]
    
#     # 단어
#     word = ''
#     in_order(1)
#     print(f'#{tc} {word}')