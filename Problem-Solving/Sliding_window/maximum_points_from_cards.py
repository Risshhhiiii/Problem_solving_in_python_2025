class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sum of first k cards (all from left side initially)
        curr_sum = sum(cardPoints[:k])
        max_sum = curr_sum  

        # try replacing cards from left with cards from right
        for i in range(1, k+1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
            max_sum = max(max_sum, curr_sum)

        return max_sum