T = int(input())
word ={"ZRO":0,
        "ONE":1,
        "TWO":2,
        "THR":3,
        "FOR":4,
        "FIV":5,
        "SIX":6,
        "SVN":7,
        "EGT":8,
        "NIN":9,
        }
num_word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T + 1):
    
    _, N = input().split()
    N = int(N)
    words = input()

    cnt = [0]*10
    for i in range(N):
        cnt[word[i]] += 1

    sorted_words = []
    for num in range(10):
        sorted_words.extend([num_word[num]]*cnt[num])
    
    print(f"#{tc}")
    print(" ".join(sorted_words))