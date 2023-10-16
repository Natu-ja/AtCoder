# https://atcoder.jp/contests/abc322/tasks/abc322_a

N = int(input())
S = list(input())

for i in range(N):
    if N > i+2:
        if (S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C'):
            print(i+1)
            break
    else:
        print(-1)
        break