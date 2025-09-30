energy = [30, 10, 60, 10, 60, 50]
n = len(energy)
dp = [-1]*(n)
dp[0] = 0
for index in range(1, n):
    jump2 = float('inf')
    jump1 = dp[index-1] + abs(energy[index] - energy[index-1])
    if index > 1:
        jump2 = dp[index-2] + abs(energy[index]-energy[index-2])
    dp[index] = min(jump1, jump2)
print(dp[n-1])