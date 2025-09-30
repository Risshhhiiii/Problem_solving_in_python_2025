l = list(map(int,input().split()))
count = 0
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for i in l :
    if isprime(i):
        count+=1
print(count)

