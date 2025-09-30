n = int(input())
police , unsolved = 0 , 0 
events = list(map(int,input().split()))
for e in events :
    if e == -1 :
        if police > 0 :
            police-=1
        else:
            unsolved+=1
    else:
        police+=e
print(unsolved)