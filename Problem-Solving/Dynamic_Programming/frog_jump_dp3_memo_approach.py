'''import sys
import math

def fun(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    jumpTwo = sys.maxsize
    jumpOne = fun(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = fun(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(fun(n-1, height, dp))

    '''

''' Direct recursive solution 

def fun(energy,index):
    if index == 0:
        return 0
    jump1 = fun(energy,index-1) + abs(energy[index]-energy[index-1])
    jump2= float('inf')
    if index > 1 :
        jump2 = fun(energy,index-2) + abs(energy[index]-energy[index-2])
    return min(jump1,jump2)

energy = [30, 10, 60, 10, 60, 50]
n = len(energy) - 1
print(fun(energy,n))

'''

def fun(energy,index,dp):
    if index == 0:
        return 0
    if dp[index]!=-1 :
        return dp[index]
    jump1 = fun(energy,index-1,dp) + abs(energy[index]-energy[index-1])
    jump2= float('inf')
    if index > 1 :
        jump2 = fun(energy,index-2,dp) + abs(energy[index]-energy[index-2])
    dp[index] = min(jump1,jump2)
    return min(jump1,jump2)

energy = [30, 10, 60, 10, 60, 50]
n = len(energy) - 1
dp = [-1]*(n+1)
print(fun(energy,n,dp))
