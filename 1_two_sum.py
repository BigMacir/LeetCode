class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len((nums))):
            for ii in range(len(nums)):
                if i == ii:
                    continue
                if nums[i] + nums[ii] == target:
                    return [i, ii]