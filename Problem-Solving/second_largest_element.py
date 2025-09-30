l = list(map(int,input().split()))
maxx = float('-inf')
maxx2 = float('-inf')
for i in l :
    if i > maxx :
        maxx2 = maxx
        maxx = i
    elif i > maxx2 and i != maxx:
        maxx2 = i

print(maxx2)