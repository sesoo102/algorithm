T = int(input())

for test_case in range(1,T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    found = 1
    # (i, j) i가 첫번재 리스트(가로), j가 리스트 속 리스트 접근(세로)

    # 가로 확인
    
    for i in range(9):
        v_sudoku = set()
        for j in range(9):
            v_sudoku.add(sudoku[i][j])
        if len(v_sudoku)==9:
            continue
                
        else:
            found = 0


                
    
    # 세로 확인
    if not found:
        for j in range(9):
            h_sudoku = set()
            for i in range(9):
                h_sudoku.add(sudoku[i][j])
            if len(h_sudoku)==9:
                continue

        else:
            found = 0

    
    # 3*3 격자
    if not found:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                    box_sudoku = set()
                    for m in range(3):
                        for n in range(3):
                            box_sudoku.add(sudoku[i+m][j+n])
                    if len(box_sudoku)==9:
                        continue
        else:
            found = 0

    result = 1 if found else 0    
    print(f"#{test_case} {result}")