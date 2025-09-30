l = list(map(int,input().split()))
key = int(input())
s,e=0,len(l)-1
while s<=e :
    mid = (s + e)//2
    if l[mid] == key:
        print("INDEX = ",mid)
        break
    elif l[mid] > key :
        e = mid -1
    elif l[mid] < key :
        s = mid + 1
else:
    print(False)