# 사칙연산
'''
실수 연산
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과에 해당 연산자를 적용
for N
    if 정점 정수:
        정점번호, 양의 정수
    elif 정점 연산자:
        정점번호, 연산자, c1, c2

'''
T = 10

def calc_val(o, l, r): # 연산자와 왼쪽값, 오른쪽값이 주어질 때 계산값 반환
    if o == '+':
        return l + r
    elif o == '-':
        return l - r
    elif o == '*':
        return l * r
    elif o == '/':
        return l / r


def calc_tree(i): # 루트노드가 i일 때 서브트리의 계산결과
    global tree, N
    if tree[i]['is_op']: # 만약 현재 루트노드 i가 연산자 노드라면? => LRV
        lft_val = calc_tree(tree[i]['lft']) # 왼쪽 자식 노드를 루트노드로 하는 트리의 계산결과
        rgt_val = calc_tree(tree[i]['rgt']) # 오른쪽 자식 노드를 루트노드로 하는 트리의 계산결과
        return calc_val(tree[i]['op'], lft_val, rgt_val)
    else: # i 번째 노드가 연산자 노드가 아니라면? 
        return tree[i]['val']



for tc in range(1, T+1):
    N = int(input()) # 트리의 노드 갯수

    # 트리를 저장하는 방법
    # 1. 완전이진트리
    # 2. 왼쪽,오른쪽 자식 배열 2개 만들기
    # 3. 부모 노드의 번호를 저앟나는 배열 1개 만들기

    tree = {} # 트리를 딕셔너리로 저장 
    # 정점번호: key, value: 노드의 내용

    for _ in range(N): # N개의 노드 정보가 주어진다.
        tokens = input().split() # 한줄 입력받아서 공백으로 쪼갠다.
        # 정수 노드: 정점번호, 숫자
        # 연산자 노드: 정점번호, 연산자, 왼쪽, 오른쪽자식 정점번호

        num = int(tokens[0]) # 정점번호
        if len(tokens) == 2: # 정수 노드
            val = int(tokens[1]) # 두번째 토큰에 정수값 
            tree[num] = {'num': num, 'is_op': False, 'val': val} # 정점번호, 연산자여부, 정수값 저장
        elif len(tokens) == 4: # 연산자 노드
            op = tokens[1] # 연산자
            lft = int(tokens[2]) # 왼쪽 자식
            rgt = int(tokens[3]) # 오른쪽 자식
            tree[num] = {'num': num, 'is_op': True, 'op': op, 'lft': lft, 'rgt': rgt}
            # 정점번호, 연산자여부, 연산자, 왼쪽자식번호, 오른쪽자식번호
    
    # 루트 노드(1번 노드)로부터 탐색을 한다.
    # postorder, 후위순회 방식.
    ans = calc_tree(1) # 1번 노드가 루트 노드일 때의 계산 결과

    print(f"#{tc} {int(ans)}")
