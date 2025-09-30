def fun(n):
    if n == 0:
        return 200
    t = fun(n-1)        # Recursive call first (go down to base case)
    print(n, end=" ")    # Print **after returning**, to get ascending order
    return t             # Return the base case value

a = 5
result = fun(a)
print(result)