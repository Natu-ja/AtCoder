# https://atcoder.jp/contests/abc322/tasks/abc322_b

N, M = input().split()
N = int(N)
S = input()
T = input()

if S == T[:N] and S == T[-N:]:
    print(0)
elif S == T[:N]:
    print(1)
elif S == T[-N:]:
    print(2)
else:
    print(3)