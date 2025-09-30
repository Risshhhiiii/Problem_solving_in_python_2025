n = int(input())
def even_copy(n):
    print(n, end=" ")
    if n > 2:
        even_copy(n-2)
        print(n, end=" ")

even_copy(n)