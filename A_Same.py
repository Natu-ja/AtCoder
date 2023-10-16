# https://atcoder.jp/contests/abc324/tasks/abc324_a

n = int(input())
l = input().split()

for i in range(n):
    if i != n-1:
        if l[i] != l[i+1]:
            print('No')
            break
    else:
        print('Yes')