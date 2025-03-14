# 이진 합

T = int(input())

def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] *(N+1)
    last = 0

    for n in arr:
        enq(n)


    ans = 0
    i = N//2
    while i != 1:
        ans += heap[i]
        i = i//2

    
    print(f"#{test_case} {ans+heap[1]}")