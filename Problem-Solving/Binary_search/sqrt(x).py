class Solution:
    def mySqrt(self, x: int) -> int:
        s,e=0,x
        while s <= e :
            m  = (s+e)//2
            if m*m == x :
                return m
            elif m*m > x :
                e = m - 1
            elif m*m < x :
                s = m + 1
        return e