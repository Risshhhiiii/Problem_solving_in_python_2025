l = list(map(int, input().split()))
s=0
for i in range(1,len(l),2):
    if l[i]%2==0:
        s+=l[i]
print(s)