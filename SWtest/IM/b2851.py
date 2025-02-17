# 슈퍼마리오

total = []
score = 0
for i in range(10):
    total.append(int(input()))

for j in total:
    score += j
    if score >= 100:
        if  score-100 > 100 - (score-j):
            score -= j
        break

print(score)  