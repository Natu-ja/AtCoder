# https://atcoder.jp/contests/abc324/tasks/abc324_b

n = int(input())
x, y = 2, 3


while n%2 == 0:
    n = n/x
while n%3 == 0:
    n = n/y

print('Yes') if n == 1 else print('No')