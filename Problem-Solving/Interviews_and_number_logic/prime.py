n = int(input())
flag = 0
for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        flag = 1
        break
if flag == 1 :
    print("Not Prime")
else:
    print("Prime")

#9 , 1281 , 1342 , 509 , 231