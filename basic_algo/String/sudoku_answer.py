T = int(input())

for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    found = False

    # 1️⃣ 가로(행) 검사
    for i in range(9):
        v_sudoku = set()
        for j in range(9):
            v_sudoku.add(sudoku[i][j])
        if len(v_sudoku) != 9:
            break
    else:
        found = True

    # 2️⃣ 세로(열) 검사
    if not found:
        for j in range(9):
            h_sudoku = set()
            for i in range(9):
                h_sudoku.add(sudoku[i][j])
            if len(h_sudoku) != 9:
                break
        else:
            found = True

    # 3️⃣ 3×3 박스 검사
    if not found:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_sudoku = set()
                for m in range(3):
                    for n in range(3):
                        box_sudoku.add(sudoku[i+m][j+n])
                if len(box_sudoku) != 9:
                    break
            else:
                continue
            break
        else:
            found = True

    result = 1 if found else 0    
    print(f"#{test_case} {result}")
