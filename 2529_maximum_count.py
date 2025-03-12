class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for number in nums:
            if number > 0:
                pos += 1
            if number < 0:
                neg += 1
        
        if pos > neg:
            return pos
        else:
            return neg