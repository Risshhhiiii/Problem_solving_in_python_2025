l = list(map(int,input().split()))
d = {}
for i in l :
    if i not in d :
        d[i]=1
    else:
        d[i] += 1
print(d)
maxx,maxx2 = 0,0
ele1 , ele2 = 0,0
for i in d:
    if d[i] > maxx:
        maxx2 = maxx
        ele2 = ele1
        maxx = d[i]
        ele1 = i
    else:
        if d[i] > maxx2 and d[i] != maxx:
            maxx2 = d[i]
            ele2 = i
print(ele2)