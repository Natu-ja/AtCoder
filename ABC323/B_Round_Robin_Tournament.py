# https://atcoder.jp/contests/abc323/tasks/abc323_b

n = int(input())
l = []
counts = []
rank = ''

for i in range(n):
    count = 0
    l.append(input())
    for j in range(n):
        if l[i][j] == 'o':
            count += 1
    counts.append([i+1, count])

counts = sorted(counts, key = lambda x:x[1], reverse = True)

for i in range(n):
    if i != 0:
        rank = rank + " " + str(counts[i][0])
    else:
        rank = str(counts[i][0])

print(rank)