text = list(input())

start, stop, step = 2, 16, 2

for i in range(start, stop+step, step):
    if int(text[i-1]) == 1:
        print('No')
        break
    else:
        if i == stop:
            print('Yes')