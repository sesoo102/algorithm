T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    q = list(map(int, input().split()))

    move = M % N
    print(f"#{test_case} {q[move]}")



# # queue
# T = int(input())

# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     queue = list(map(int, input().split()))
    
#     for i in range(m):
#         queue.append(queue.pop(0))
    
#     print(f"#{test_case} {queue[0]}")
    