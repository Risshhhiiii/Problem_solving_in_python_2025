class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        maxx = 0
        for i in nums :
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d :
            if i+1 in d and d[i] + d[i+1] > maxx :
                maxx = d[i] +  d[i+1]
        return maxx