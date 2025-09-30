class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        n = e
        if len(nums)==1 :
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[n] > nums[n-1]:
            return n
        while s<=e :
            mid = (s+e)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1] :
                return mid
            elif nums[mid] < nums[mid+1]:
                s = mid+1
            elif nums[mid] > nums[mid+1]:
                e = mid-1