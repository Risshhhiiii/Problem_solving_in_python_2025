arr = [1,2,5,10]
target = 12
n = len(arr)
dp = []
for i in range(n+1):
    dp.append([0]*(target+1))

for i in range(n+1):
    dp[i][0] = 1

for i in range(1,n+1):
    for j in range(1,target+1):
        if arr[i-1]>j :
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j-arr[i-1]]

if dp[n][target] :
    print("IT'S POSSIBLE..")
else:
    print("IT'S NOT POSSIBLE")

for row in dp :
    print(row)