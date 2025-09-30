class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        max_sum = s
        for i in range(1,len(nums)-k+1):
            s = s - nums[i-1] + nums[i+k-1]
            max_sum = max(s,max_sum)
        return max_sum / k