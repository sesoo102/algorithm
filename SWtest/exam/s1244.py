# 최대상금
T = int(input())
for test_case in range(1, T+1):
    num_board, N = map(str, input().split())
    n = int(N)
    n_list = [int(num_board[i]) for i in range(len(num_board))]
    
    if sorted(n_list, reverse=True) == n_list and n % 2 == 1:
        n_list[-1], n_list[-2] = n_list[-2], n_list[-1]
        result = n_list
    