a = int(input())

def fun(n,m=0):
    if m>n-2 :
        print(m+1,end=" ")
        return
    print(m+1,end = " ")
    fun(n,m+1)
    print(m+1,end = " ")
fun(a)