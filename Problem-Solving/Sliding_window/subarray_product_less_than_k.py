class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:        
        l,r=0,0
        product , count = 1 , 0
        if k<=1:
            return 0
        while r < len(nums):
            product*=nums[r]
            while product >= k :
                product//=nums[l]
                l+=1
            count = count + (r-l+1)
            r+=1
        return(count)