class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(piles,h,m):
            res = 0
            for p in piles :
                res+=math.ceil(p/m)
            if res > h :
                return False
            else:
                return True
        
        s,e=1,max(piles)
        while s<=e :
            mid = (s+e)//2
            if is_possible(piles,h,mid):
                e = mid - 1 
            else : 
                s = mid + 1
        return s