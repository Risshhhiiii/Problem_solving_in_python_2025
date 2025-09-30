class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        c = nums[0]

        for i in nums :
            if vote == 0:
                c = i
            if c == i :
                vote+=1
            else:
                vote-=1
        return c