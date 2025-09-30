a = int(input("enter the number of rows : "))
for i in range (0 , a):
    newrow = a-i
    print(" " * (newrow -1 ), end='')
    print("*" * (i+1))
   
