l = list(map(int,input().split()))
d = {}
for i in l :
    if i not in d :
        d[i]=1
    else:
        d[i] += 1
print(d)
maxx = 0
ele = 0
for i in d:
    if d[i] > maxx:
        maxx = d[i]
        ele = i
print(ele)