a = int(input())

def fun(n):
    print(n,end=" ")
    if n > 1 :
        fun(n-1)
        print(n,end = " ")

fun(a)