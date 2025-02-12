T = int(input())
days = {
    "01":31, "02":28, "03":31, "04":30,
    "05":31, "06":30, "07": 31, "08":31,
    "09":30, "10":31 , "11":30, "12":31
      }

for test_case in range(1, T+1):
    arr = list(map(int, input()))

    year = arr[0:4]
    month = arr[4:6]
    day = arr[6:8]

    if int(year) == 00:
        print(f'#{test_case} -1')
        continue
    
    if month not in days:
        print(f'#{test_case} -1')
        continue

    max_day = days[month]
    if int(day) < 1 or int(day) > max_day:
        print(f'#{test_case} -1')
        continue

    print(f'#{test_case} {year}/{month}/{day}')
