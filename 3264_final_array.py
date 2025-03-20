class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minimum = min(nums)
            for index, number in enumerate(nums):
                if number == minimum:
                    nums[index] *= multiplier
                    break
        return nums