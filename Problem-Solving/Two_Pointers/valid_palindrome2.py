class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        while l < r :
            if s[l]!= s[r]:
                r_s = s[l+1 : r+1]
                l_s = s[l:r]
                if (r_s == r_s[::-1]) or (l_s == l_s[::-1]):
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True