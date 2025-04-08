T = int(input())

def is_baby_gin(p):
    cnt = 0
    a, b, c = p[0], p[1], p[2]
    if a == b == c:
        cnt += 1
    elif a == b-1 == c-2 :
        cnt += 1
    
    a, b, c = p[3], p[4], p[5]
    if a == b == c:
        cnt += 1
    elif a == b-1 == c-2:
        cnt += 1
    
    return cnt == 2



def make_permutation(cnt):
    global baby_gin_result
    if cnt == 6:
        if is_baby_gin(path):
            baby_gin_result = True
            return
    
    for idx in range(6):
        if used[idx]:
            continue
        path.append(arr[idx])
        used[idx] = 1
        make_permutation(cnt+1)
        used[idx] = 0
        path.pop()




for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    path = []
    used = [0] * 6
    baby_gin_result = False

    make_permutation(0)

    print(f"{test_case} {baby_gin_result}")