class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,m=0,0
        d={}
        for r in range(len(s)):
            val = s[r]
            if val not in d :
                d[val] = r
            else:
                if d[val] >= l :
                    l = d[val]+1
                d[val] = r
            m = max(m,r-l+1)
        return m