# subtree

T = int(input())

def pre_order(T):
    global cnt
    if T:
        cnt += 1
        pre_order(c1[T])
        pre_order(c2[T])

for test_case in range(1, T+1):
    E, N = list(map(int, input().split()))
    # 노드 번호는 1번 부터 E+1번까지 존재
    arr = list(map(int, input().split()))

    c1 = [0] * (E+2)
    c2 = [0] * (E+2)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]

        # 부모 노드를 인덱스로 자식 번호 저장
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    # print(c1)
    # print(c2)
    cnt = 0
    pre_order(N)
    print(f"#{test_case} {cnt}")