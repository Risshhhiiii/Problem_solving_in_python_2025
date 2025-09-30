n = 5
a=0
b=1
for i in range(2,n+1):
    fib=a+b
    a=b
    b=fib
print(fib)