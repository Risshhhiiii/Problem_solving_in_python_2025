l = list(map(int, input().split()))
low,high = map(int,input().split())
p = 1
for i in l:
    if i >= low and i<=high:
        p*=i
print(p)